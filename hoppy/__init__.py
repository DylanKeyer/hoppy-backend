from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URI')
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
app.config['SQLALCHEMY_POOL_SIZE'] = 5
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# enable CORS so Angular frontend can generate requests
cors = CORS(app)
# initialize flask-sqlalchemy
db = SQLAlchemy(app)
# initialize flask-marshmallow api
ma = Marshmallow(app)
# migrate changes
migrate = Migrate(app, db)

from hoppy.api.resources import BeerResource, BreweryResource, BreweryVenueResource
api = Api(app)
api.add_resource(BreweryResource, '/api/brewery', '/api/brewery/<id>')
api.add_resource(BeerResource, '/api/beer', '/api/beer/', '/api/beer/<id>')
api.add_resource(BreweryVenueResource, '/api/brewery/<brewery_id>/venues', '/api/brewery/venues/' # for posts)
