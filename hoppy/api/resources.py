from flask import request
from flask_restful import Resource
import logging

from hoppy import app, db
from ..entities.models import Beer, Brewery
from ..entities.schemas import BeerSchema, BrewerySchema
beer_schema = BeerSchema(strict=True)
beers_schema = BeerSchema(many=True)
brewery_schema = BrewerySchema(strict=True)
breweries_schema = BrewerySchema(many=True)
# @app.route('/api/beers/', methods=['GET','POST'])
# def beers():
#     if request.method == 'POST':
#         posted_beer = beer_schema.load(request.get_json())
#         db.session.add(posted_beer.data)
#         db.session.commit()
#         return 'Success'
#     else:       
#         all_beers = Beer.query.all()
#         return beer_schema.jsonify(all_beers)

# @app.route('/api/beers/<id>')
# def beer_detail(id):
#     if request.method == 'POST':
#         posted_beer = beer_schema.load(request.get_json())
#         beer = Beer(**posted_beer.data)
#         db.session.add(beer)
#         db.session.commit()
#     elif request.method == 'GET':
#         beer = Beer.query.filter_by(id=id).first()
#         return beer_schema.jsonify(beer)

class BeerResource(Resource):
    def get(self, id=None):
        # fetch beers from database
        if id is None:
            beer_objects = db.session.query(Beer).all()
            return beers_schema.jsonify(beer_objects)
        else:
            beer_objects = db.session.query(Beer).filter_by(id=id)
                
            return beer_schema.jsonify(beer_objects)
    
    def post(self):
        print(request.get_json(force=True))
        posted_beer = request.get_json()
        print(beer_schema.dump(posted_beer).data)
        beer = Beer(**beer_schema.dump(posted_beer).data)
        db.session.add(beer)
        db.session.commit()
        return "Success"

class BreweryResource(Resource):
    def get(self, id=None):
        if id is None:
            brewery_objects = db.session.query(Brewery).all()
            return breweries_schema.jsonify(brewery_objects)
        else:
            brewery_objects = db.session.query(Brewery).filter_by(id=id)        
            return brewery_schema.jsonify(brewery_objects)

    def post(self):
        # serialize posted JSON to a marshmallow schema object
        posted_brewery = request.get_json(force=True)
        brewery,errors = brewery_schema.load(posted_brewery)
        db.session.add(brewery)
        db.session.commit()
        
        return "Success"