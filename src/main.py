from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS
from datetime import datetime

from .entities.entity import Session, engine, Base
from .entities.models import Beer, Brewery, Venue, User, Review, UserSocialMedia, BeerType
from .entities.schemas import BeerSchema, BrewerySchema, VenueSchema, UserSchema, ReviewSchema, UserSocialMediaSchema
from .api.resources import BeerResource, BreweryResource

# generate database schema
Base.metadata.create_all(engine)

# generate Flask app
app = Flask(__name__)

# enable CORS so Angular frontend can generate requests
CORS(app)

# enable flask-restful API functionality
api = Api(app)

# add resources with endpoints to API
api.add_resource(BeerResource, '/api/beer', '/api/beer/', '/api/beer/<beer_id>')
api.add_resource(BreweryResource, '/api/brewery', '/api/brewery/', '/api/brewery/<brewery_id>')

if __name__ == '__main__':
    app.run(debug=True)