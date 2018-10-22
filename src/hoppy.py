from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

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

@app.route('/beers', methods=['GET', 'POST'])
def beers():
    if request.method == 'GET':
        # fetch beers from database
        session = Session()
        beer_objects = session.query(Beer).all()
        
        # transform to serializable format for JSON
        beer_schema = BeerSchema(many=True)
        beers, errors = beer_schema.dump(beer_objects)
        
        # serialize to JSON
        session.close()
        return jsonify(beers)
    elif request.method == 'POST':
        # serialize posted JSON to a marshmallow schema object
        posted_beer = BeerSchema()\
        .load(request.get_json())

        beer = Beer(**posted_beer.data)
        session = Session()
        session.add(beer)
        session.commit()
        
        session.close()
        return jsonify(
            HTTP_STATUS=200,
            result='Success',
            beer: request.get_json(),
            utc_timestamp: datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            timestamp: datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

@app.route('/breweries', methods=['GET', 'POST'])
def add_breweries():

    
    
    
@app.route
def add_breweries():
     if request.method == 'GET':
        # fetch breweries from database
        session = Session()
        brewery_objects = session.query(Brewery).all()
        
        # transform to serializable format for JSON
        brewery_schema = BrewerySchema(many=True)
        breweries, errors = brewery_schema.dump(brewery_objects)
        
        # serialize to JSON
        session.close()
        return jsonify(breweries)

    elif request.method == 'POST':
        # serialize posted JSON to a marshmallow schema object
        posted_brewery = BrewerySchema()\
        .load(request.get_json())

        brewery = Brewery(**posted_brewery.data)
        session = Session()
        session.add(brewery)
        session.commit()
        
        session.close()
        return jsonify(
            HTTP_STATUS=200,
            result='Success',
            beer: request.get_json(),
            utc_timestamp: datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            timestamp: datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
    