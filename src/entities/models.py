from sqlalchemy import Column, String, Integer, Float, Text, Enum
from sqlalchemy import ForeignKey
from .entity import Base, Entity
from .enums import BeerType, BreweryType, SocialMediaType, ServingType
	
class Beer(Entity, Base):
    __tablename__ = 'beer'
    '''Constraints'''
    brewery_id = Column(Integer, ForeignKey("brewery.id"), nullable=False)
    '''Non-constraint columns'''
    beer_type = Column(Enum(BeerType))
    beer_name = Column(String(32), nullable=False)
    description = Column(Text)
    abv = Column(Float)
    ibu = Column(Integer)

class Brewery(Entity, Base):
    __tablename__ = 'brewery'
    '''Constraints'''
    brewery_type = Column(Enum(BreweryType), nullable=False)
    '''Non-constraint columns'''
    brewery_name = Column(String(32), nullable=False)
    description = Column(Text)
	
class User(Entity, Base):
    __tablename__ = 'user'
    '''Constraints'''
    '''Non-constraint columns'''
    brewery_name = Column(String(32), nullable=False)
    description = Column(Text)
    
class Venue(Entity, Base):
    __tablename__ = 'venue'
    '''Constraints'''
    '''Non-constraint columns'''
    venue_name = Column(String(32), nullable=False)
    location = Column(String(64))
    longitude = Column(Float)
    latitude = Column(Float)
	
class Review(Entity, Base):
    __tablename__ = 'review'
    '''Constraints'''
    beer_id = Column(Integer, ForeignKey('beer.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venue.id'), nullable=False)
    serving_type = Column(Enum(ServingType), nullable=True)
    '''Non-constraint columns'''
    title = Column(Text)
    description = Column(Text)
    rating = Column(Float)

class UserSocialMedia(Base):
    __tablename__ = 'user_social_media'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    link = Column(Text, nullable=False)
    social_media_type = Column(Enum(SocialMediaType), nullable=False)
