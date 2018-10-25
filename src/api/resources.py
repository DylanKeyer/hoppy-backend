from flask_restful import Resource
from flask import request, jsonify

from ..entities.entity import Session, engine, Base
from ..entities.models import Beer, Brewery, Venue, User, Review, UserSocialMedia, BeerType, SysUser, SysUserAccount
from ..entities.schemas import BeerSchema, BrewerySchema, VenueSchema, UserSchema, ReviewSchema, UserSocialMediaSchema
from ..entities.schema import SysUserSchema

from .base import api_response

class SysUserResource(Resource):
    def get(self, sys_user_id):
        session = Session()
        sys_user_schema = SysUserSchema()

class BeerResource(Resource):
    def get(self, beer_id=None):
        # fetch beers from database
        session = Session()
        if beer_id is None:
            beer_objects = session.query(Beer).all()
        else:
            beer_objects = session.query(Beer).filter(Beer.id == beer_id)
        
        # transform to serializable format for JSON
        beer_schema = BeerSchema(many=True)
        beers, errors = beer_schema.dump(beer_objects)
        
        # serialize to JSON
        session.close()
        return jsonify(beers)
    
    def post(self):
        posted_beer = BeerSchema()\
        .load(request.get_json())

        beer = Beer(**posted_beer.data)
        session = Session()
        session.add(beer)
        session.commit()
        
        session.close()
        return api_response(200, "Success", "", request)

class BreweryResource(Resource):
    def get(self, brewery_id=None):
        # fetch breweries from database
        session = Session()

        if brewery_id is None:
            brewery_objects = session.query(Brewery).all()
        else:
            brewery_objects = session.query(Brewery).filter(Brewery.id == brewery_id)
        
        # transform to serializable format for JSON
        brewery_schema = BrewerySchema(many=True)
        breweries, errors = brewery_schema.dump(brewery_objects)
        
        # serialize to JSON
        session.close()
        return jsonify(breweries)

    def post(self):
        # serialize posted JSON to a marshmallow schema object
        posted_brewery = BrewerySchema()\
        .load(request.get_json())

        brewery = Brewery(**posted_brewery.data)
        session = Session()
        session.add(brewery)
        session.commit()
        
        session.close()
        return api_response(200, "Success", "", request)