from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.models import Beer, Brewery, Venue, User, Review, UserSocialMedia, BeerType
from .entities.schemas import BeerSchema, BrewerySchema, VenueSchema, UserSchema, ReviewSchema, UserSocialMediaSchema

app= Flask(__name__)
CORS(app)
# generate database schema
Base.metadata.create_all(engine)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/beers')
def get_beers():
    # fetch beers from database
    session = Session()
    beer_objects = session.query(Beer).all()
    
    # transform to serializable format for JSON
    beer_schema = BeerSchema(many=True)
    beers, errors = beer_schema.dump(beer_objects)
    
    # serialize to JSON
    session.close()
    return jsonify(beers)

@app.route('/beers', methods=['POST'])
def add_beers():
    posted_beer = BeerSchema()\
        .load(request.get_json())
    beer = Beer(**posted_beer.data)
    
    session = Session()
    session.add(beer)
    session.commit()
    
    session.close()
    return 'Beer successfully added'
    
    