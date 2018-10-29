# from passlib.apps import custom_app_context as pwd_context
from hoppy import db
from .enums import BeerType, BreweryType, SocialMediaType, ServingType

class Brewery(db.Model):
    __tablename__ = 'brewery'
    '''Constraints'''
    id = db.Column(db.Integer, primary_key=True)
    '''Non-constraint columns'''
    brewery_type = db.Column(db.Enum(BreweryType), nullable=False)
    brewery_name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text)
    created_dtm = db.Column(db.DateTime)
    updated_dtm = db.Column(db.DateTime)

class Beer(db.Model):
    __tablename__ = 'beer'
    '''Constraints'''
    id = db.Column(db.Integer, primary_key=True)
    brewery_id = db.Column(db.Integer, db.ForeignKey("brewery.id"), nullable=False)
    brewery = db.relationship("Brewery", foreign_keys=brewery_id)
    '''Non-constraint columns'''
    beer_type = db.Column(db.Enum(BeerType))
    beer_name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text)
    abv = db.Column(db.Float)
    ibu = db.Column(db.Integer)
    created_dtm = db.Column(db.DateTime)
    updated_dtm = db.Column(db.DateTime)

# SQLALCHEMY STUFF #
# class Beer(Entity, Base):
#     __tablename__ = 'beer'
#     '''Constraints'''
#     brewery_id = Column(Integer, ForeignKey("brewery.id"), nullable=False)
#     '''Non-constraint columns'''
#     beer_type = Column(Enum(BeerType))
#     beer_name = Column(String(32), nullable=False)
#     description = Column(Text)
#     abv = Column(Float)
#     ibu = Column(Integer)

# class Brewery(Entity, Base):
#     __tablename__ = 'brewery'
#     '''Constraints'''
#     brewery_type = Column(Enum(BreweryType), nullable=False)
#     '''Non-constraint columns'''
#     brewery_name = Column(String(32), nullable=False)
#     description = Column(Text)
	
# class User(Entity, Base):
#     __tablename__ = 'user'
#     '''Constraints'''
#     '''Non-constraint columns'''
#     user_name = Column(String(32), nullable=False)
#     description = Column(Text)
    
# class Venue(Entity, Base):
#     __tablename__ = 'venue'
#     '''Constraints'''
#     '''Non-constraint columns'''
#     venue_name = Column(String(32), nullable=False)
#     location = Column(String(64))
#     longitude = Column(Float)
#     latitude = Column(Float)
	
# class Review(Entity, Base):
#     __tablename__ = 'review'
#     '''Constraints'''
#     beer_id = Column(Integer, ForeignKey('beer.id'), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#     venue_id = Column(Integer, ForeignKey('venue.id'), nullable=False)
#     serving_type = Column(Enum(ServingType), nullable=True)
#     '''Non-constraint columns'''
#     title = Column(Text)
#     description = Column(Text)
#     rating = Column(Float)

# class UserSocialMedia(Base):
#     __tablename__ = 'user_social_media'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#     link = Column(Text, nullable=False)
#     social_media_type = Column(Enum(SocialMediaType), nullable=False)
# ##SYSTEM TABLES##
# class Tenant(Base):
#     __tablename__ = 'sys_tenants'
#     '''Contains all base tenant information'''
#     id = Column(Integer, primary_key=True)
#     country_code = Column(String(2), nullable=False) # 2-digit ISO code
#     organization_name = Column(Text, nullable=False) # company name
#     administrative_area = Column(String(64), nullable=False) # state/province/region
#     sub_administrative_area = Column(String(64)) # district/county
#     locality = Column(String(128), nullable=False) # city/town
#     dependent_locality = Column(String(128)) # unused for now
#     postal_code = Column(String(32), nullable=False) # postal code/ZIP code
#     thoroughfare = Column(Text, nullable=False) # street address
#     premise = Column(String(32)) # apartment/suite/box number
#     sub_premise = Column(String(32)) # sub-premise

# class TenantToBreweryMM(Base):
#     __tablename__ = 'sys_tenant_brewery_MM'
#     '''Maps the tenant to the breweries that they own and have rights to'''
#     '''Constraints'''
#     id = Column(Integer, primary_key=True)
#     tenant_id = Column(Integer, ForeignKey('tenant.id'), nullable=False)

# class SysUser(Base):
#     __tablename__ = 'sys_user'
#     id = Column(Integer, primary_key=True)
#     person_number = Column(String(16), nullable=False)
#     tenant_id = Column(Integer, ForeignKey('tenant.id'), nullable=False)
    
# class SysUserAccount(Base):
#     __tablename__ = 'sys_user_account'
#     sys_user_id = Column(Integer, ForeignKey('sys_user.id'), nullable=False)
#     email = Column(String(64), nullable=False)
#     username = Column(String(64), nullable=False)
#     password_hash = Column(String(128), nullable=False)

#     def hash_password(self, plain_text_password):
#         self.password_hash = pwd_context.encrypt(plain_text_password)

#     def verify_password(self, plain_text_password):
#         return pwd_context.verify(plain_text_password, self.password_hash)