from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.models import Beer, Brewery, Venue, User, Review, UserSocialMedia
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
    
    # transforn to serializable form format for JSON
    beer_schema = BeerSchema(many=True)
    beers = beer_schema.dump(beer_objects)
    
    # serialize to JSON
    session.close()
    return jsonify(beers)

@app.route('/beers', methods=['POST'])
def add_beers():
    posted_beer = BeerSchema()\
        .load(request.get_json())
    beer = Beer(**posted_beer.data, id='1')
    
    session = Session()
    session.add(beer)
    session.commit()
    
    new_beer = BeerSchema().dump(beer).data
    session.close()
    return jsonify(new_beer), 201
    return 'Beer successfully added'
    
    