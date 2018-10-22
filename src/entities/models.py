from sqlalchemy import Column, String, Integer, Float, Text, Enum
from sqlalchemy import ForeignKey
from .entity import Base, Entity
from .enums import BeerType, BreweryType, SocialMediaType, ServingType

##SYSTEM TABLES##
class Tenant(Base):
    __tablename__ = 'sys_tenants'
    '''Contains all base tenant information'''
    id = Column(Integer, primary_key=true)
    country_code = Column(String(2), nullable=False) # 2-digit ISO code
    organization_name = Column(Text, nullable=False) # company name
    administrative_area = Column(String(64), nullable=False) # state/province/region
    sub_administrative_area = Column(String(64)) # district/county
    locality = Column(String(128), nullable=False) # city/town
    dependent_locality = Column(String(128)) # unused for now
    postal_code = Column(String(32), nullable=False) # postal code/ZIP code
    thoroughfare = Column(TEXT, nullable=False) # street address
    premise = Column(String(32)) # apartment/suite/box number
    sub_premise = Column(String(32)) # sub-premise

class TenantToBreweryMM(Base):
    __tablename__ = 'sys_tenant_brewery_MM'
    '''Maps the tenant to the breweries that they own and have rights to'''
    '''Constraints'''
    tenant_id = Column(Integer, ForeignKey('tenant.id'), nullable=False)


class User(Base):
    __tablename__ = 'sys_users'
    tenant_id = Column(Integer, ForeignKey('tenant.id'), nullable=False)

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
