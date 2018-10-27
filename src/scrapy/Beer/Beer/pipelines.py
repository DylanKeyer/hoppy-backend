from Beer.items import Beer, Brewery, BeerReview, User, Venue
import MySQLdb

class HoppyPipeline(object):
    def __init__(self):
        self.__base_url = 'http://localhost:5000/'
        self.url = self.__base_url
    
    def process_item(self, item, spider):
        if isinstance(item, Beer):
            self.url += 'beer' 
        elif isinstance(item, Brewery):
            self.url += 'brewery'

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
        elif isinstance(item, BeerReview):
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
