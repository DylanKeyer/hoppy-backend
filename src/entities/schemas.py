from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from .enums import BeerType, BreweryType, SocialMediaType, ServingType

class SysUserSchema(schema):
    id = fields.Number()
    person_number = fields.String()

class BeerSchema(Schema):
    id = fields.Number()
    brewery_id = fields.Number()
    '''Non-constraint columns'''
    beer_name = fields.Str()
    beer_type = EnumField(BeerType, by_value=True)
    description = fields.Str()
    abv = fields.Number()
    ibu = fields.Number()
    created_dtm = fields.DateTime()
    updated_dtm = fields.DateTime()  

class BrewerySchema(Schema):
    '''Constraints'''
    id = fields.Number()
    brewery_type = EnumField(BreweryType)
    '''Non-constraint columns'''
    brewery_name = fields.Str()
    description = fields.Str()
	
class UserSchema(Schema):
    '''Constraints'''
    id = fields.Number()
    '''Non-constraint columns'''
    user_name = fields.Str()
    description = fields.Str()
    created_dtm = fields.DateTime()
    updated_dtm = fields.DateTime() 
    
class VenueSchema(Schema):
    '''Constraints'''
    id = fields.Number()
    '''Non-constraint columns'''
    venue_name = fields.Str()
    location = fields.Str()
    longitude = fields.Number()
    latitude = fields.Number()
    created_dtm = fields.DateTime()
    updated_dtm = fields.DateTime() 
	
class ReviewSchema(Schema):
    '''Constraints'''
    id = fields.Number()
    beer_id = fields.Number()
    user_id = fields.Number()
    venue_id = fields.Number()
    serving_type = EnumField(ServingType)
    '''Non-constraint columns'''
    title = fields.Str()
    description = fields.Str()
    rating = fields.Number()
    created_dtm = fields.DateTime()
    updated_dtm = fields.DateTime()  
	
class UserSocialMediaSchema(Schema):
    user_id = fields.Number()
    social_media_type = EnumField(SocialMediaType)
    link = fields.Str()
	
