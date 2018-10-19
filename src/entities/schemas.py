from marshmallow import Schema, fields

class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()

class BeerSchema(Schema):
    id = fields.Number()
    brewery_id = fields.Number()
    '''Non-constraint columns'''
    beer_name = fields.Str()
    description = fields.Str()
    abv = fields.Number()
    ibu = fields.Number()
    created_dtm = fields.DateTime()
    updated_dtm = fields.DateTime()  

class BrewerySchema(Schema):
    '''Constraints'''
    id = fields.Number()
    brewery_type_id = fields.Number()
    '''Non-constraint columns'''
    brewery_name = fields.Str()
    description = fields.Str()
	
class UserSchema(Schema):
    '''Constraints'''
    id = fields.Number()
    '''Non-constraint columns'''
    brewery_name = fields.Str()
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
    serving_type_id = fields.Number()
    '''Non-constraint columns'''
    title = fields.Str()
    description = fields.Str()
    rating = fields.Number()
    created_dtm = fields.DateTime()
    updated_dtm = fields.DateTime()  
	
class UserSocialMediaSchema(Schema):
    user_id = fields.Number()
    social_media_type_id = fields.Number()
    link = fields.Str()
	
