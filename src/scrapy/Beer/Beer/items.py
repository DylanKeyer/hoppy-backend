from scrapy import Item, Field 

class Beer(Item):
    id = Field()
    beer__name = Field()
    brewery_id = Field()
    beer_style = Field()
    abv = Field()
    ibu = Field()
    description = Field()
    creation_dtm = Field()
    updated_dtm = Field()

class Brewery(Item):
    id = Field()
    name = Field()
    brewery_type = Field()
    description = Field()
    created_dtm = Field()
    updated_dtm = Field()

class BreweryLocation(Item):
    brewery_id = Field()
    name = Field()
    longitude = Field()
    latitude = Field()
    location = Field()

class Venue(Item):
    id = Field()
    name = Field()
    location = Field()
    latitude = Field()
    longitude = Field()
    
class Review(Item):
    id = Field()
    rating = Field()
    user_id = Field()
    serving_type = Field()
    description = Field()
    title = Field()
    beer_id = Field()
    venue_id = Field()
    created_dtm = Field()
    updated_dt = Field()
    
class User(Item):
    id = Field()
    name = Field()
    #facebook = Field()
    
    
