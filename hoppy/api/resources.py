from flask import request
from flask_restful import Resource
import logging
from marshmallow_enum import EnumField

from hoppy import app, db
from ..entities.models import Beer, Brewery, Venue, User, Review, BreweryVenue
from ..entities.schemas import BeerSchema, BrewerySchema, VenueSchema, UserSchema, ReviewSchema, BreweryVenueSchema

#initialize schemas
beer_schema = BeerSchema(strict=True)
beers_schema = BeerSchema(many=True)
brewery_schema = BrewerySchema(strict=True)
breweries_schema = BrewerySchema(many=True)
brewery_venue_schema = BrewerySchema(strict=True)
brewery_venues_schema = BrewerySchema(many=True)

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
        posted_beer = request.get_json(force=True)
        beer, errors = beer_schema.load(posted_beer)
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
        brewery, errors = brewery_schema.load(posted_brewery)
        db.session.add(brewery)
        db.session.commit()
        return "Success"

class BreweryVenueResource(Resource):
    def get(self, brewery_id=None):
        if id is None:
            return 'Must supply Brewery ID'
        else:
            brewery_venue_objects = db.session.query(BreweryVenue).filter_by(brewery_id=brewery_id)        
            return brewery_venues_schema.jsonify(brewery_venue_objects)

    def post(self):
        # serialize posted JSON to a marshmallow schema object
        posted_brewery_venue = request.get_json(force=True)
        brewery_venue, errors = brewery_venue.load(posted_brewery_venue)
        db.session.add(brewery_venue)
        db.session.commit()
        return "Success"