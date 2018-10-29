from Beer.items import Beer, Brewery, Review, User, Venue
# from ...hoppy import db
# from ...hoppy.entities.schemas import BeerSchema, BrewerySchema
# from ...hoppy.entities.models import Beer, Brewery
import MySQLdb
import json
import requests
import logging

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.json', 'w+')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        dictionary = dict(item)
        line = json.dumps(dictionary) + "\n"
        self.file.write(line)
        return item

class PostgreSQLPipeline(object):
    def __init__(self):
        pass
    
    # def process_item(self, item, spider):
    #     if isinstance(item, Beer):
    #         r = requests.post(self.urls['beer'], data=json_data)
    #     elif isinstance(item, Brewery):
    #         r = requests.post(self.urls['brewery'], data=json_data)

class HoppyAPIPipeline(object):
    def __init__(self):
        self.__base_url = 'http://localhost:5000/api/'
        self.urls = {
            'beer': self.__base_url + 'beer',
            'brewery': 'http://localhost:5000/api/brewery'
        }
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    def process_item(self, item, spider):
        json_data = json.dumps(dict(item))
        if isinstance(item, Beer):
            r = requests.post(self.urls['beer'], data=json_data)
        elif isinstance(item, Brewery):
            r = requests.post(self.urls['brewery'], data=json_data)
        return item

class MySQLPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'Steelers$1', 
                                    'untappd', charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider): 
        columns = [field for field in item.fields.keys()]
        for column in columns:
            if column not in item:
                item[column] = None
        if isinstance(item, Beer):
            self.replace_into("""REPLACE INTO untappd.beer (beer_id, name, description, abv, ibu, 
                                                            created_dtm, updated_dtm, brewery_id) 
                                   VALUES (%(beer_id)s, %(name)s, %(description)s,
                                           %(abv)s, %(ibu)s, %(created_dtm)s,
                                           %(updated_dtm)s, %(brewery_id)s)""", item)
        elif isinstance(item, Brewery):
            self.replace_into("""REPLACE INTO untappd.brewery (brewery_id, name, description,
                                                                brewery_type_id, created_dtm, updated_dtm) 
                                   VALUES (%(brewery_id)s, %(name)s, %(description)s, 
                                            %(brewery_type_id)s, %(created_dtm)s), %(updated_dtm)s""", item)
        elif isinstance(item, Review):
            self.replace_into("""REPLACE INTO beer.review (review_id, user_id, beer_id, title, text,
                                                              created_dtm, rating, serving_type_id, venue_id) 
                                   VALUES (%(review_id)s, %(user_id)s, %(beer_id)s, %(title)s, %(text)s,
                                           %(created_dtm)s, %(rating)s, %(serving_type_id)s, %(venue_id)s)""", item)
    
    def replace_into(self, sql, item):
        try:
            self.cursor.execute(sql, dict(item))
            self.conn.commit()            
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            print('Item: ')
            print(dict(item))
        return item
