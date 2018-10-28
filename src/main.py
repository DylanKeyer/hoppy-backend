from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from datetime import datetime

from .entities.entity import Session, engine, Base
from .entities.models import Beer, Brewery, Venue, User, Review, UserSocialMedia, BeerType
from .entities.schemas import BeerSchema, BrewerySchema, VenueSchema, UserSchema, ReviewSchema, UserSocialMediaSchema
from .api.resources import BeerResource, BreweryResource

# generate Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
# enable CORS so Angular frontend can generate requests
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# initialize flask-sqlalchemy
db = SQLAlchemy(app)
# initialize flask-marshmallow api
ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)