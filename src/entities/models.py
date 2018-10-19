from sqlalchemy import Column, String, Integer, Float, Text
from sqlalchemy import ForeignKey, UniqueConstraint
from .entity import Base, Entity

class UserSocialMediaType(Base):
    __tablename__ = 'user_social_media_type'
    id = Column(Integer, primary_key=True)
    user_social_media_type_name = Column(String(32), nullable=False)
    UniqueConstraint('user_social_media_type_name')
    
class BreweryType(Base):
    __tablename__ = 'brewery_type'
    id = Column(Integer, primary_key=True)
    brewery_type_name = Column(String(64), nullable=False)
    UniqueConstraint('brewery_type_name')

class ServingType(Base):
    __tablename__ = 'serving_type'
    id = Column(Integer, primary_key=True)
    brewery_type_name = Column(String(64), nullable=False)
    UniqueConstraint('serving_type_name')
	
class Beer(Entity, Base):
    __tablename__ = 'beer'
    '''Constraints'''
    brewery_id = Column(Integer, ForeignKey("brewery.id"), nullable=False)
    '''Non-constraint columns'''
    beer_name = Column(String(32), nullable=False)
    description = Column(Text)
    abv = Column(Float)
    ibu = Column(Integer)

class Brewery(Entity, Base):
    __tablename__ = 'brewery'
    '''Constraints'''
    brewery_type_id = Column(Integer, ForeignKey("brewery_type.id"), nullable=False)
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
    serving_type_id = Column(Integer, ForeignKey('serving_type.id'), nullable=True)
    '''Non-constraint columns'''
    title = Column(Text)
    description = Column(Text)
    rating = Column(Float)

class UserSocialMedia(Base):
    __tablename__ = 'user_social_media'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    link = Column(Text, nullable=False)
    social_media_type_id = Column(Integer, ForeignKey('user_social_media_type.id'), 
                                  nullable=False)
