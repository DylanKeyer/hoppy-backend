# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request, FormRequest
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from dateutil import parser
import logging
import re
import pandas

from Beer.items import Beer, Brewery, BeerReview, Venue, User

logging.basicConfig(filename='untappd.log', level=logging.DEBUG)

class UntappdSpider(Spider):
    name = 'Untappd'
    allowed_domains = ['untappd.com']
    def __init__(self):       
        self.domain = 'https://untappd.com'
        self.login_url = self.domain + '/login/'
        self.start_urls = [self.login_url]
        self.search_url = self.domain + '/search'
        self.offset = 0
        self.brewery_beer_counter = {}

    def parse(self, response):
        return FormRequest.from_response(
                response, formdata={'username':'DylanKeyer', 'password':'Steelers1'}, callback=self.search)
        
    def search(self, response):
        yield Request((self.search_url + '?' + urlencode({'q':'""', 'type':'brewery'})), callback=self.parse_search)
        
    def parse_search(self, response):
        soup = BeautifulSoup(response.body.decode('utf-8'), 'lxml')
        breweries = soup.findAll('div', {'class':'beer-item '})
        for brewery in brewery:
            self.offset += 1           
            brewery_url = self.domain + brewery.a['href']
            yield Request(brewery_url, callback=self.parse_brewery_url)

        more_breweries = soup.find('a', {'class':'more_search'})
        if more_breweries:
            logging.debug('More breweries found!')
            yield Request(self.search_url + 'search/more_search/brewery?offset={}&q=beer&sort=all'.format(str(self.offset)),
                          callback=self.parse_search)
        else:
            logging.debug('No breweries left.')
            
    def parse_reviews(self, response):
        beer_item = response.meta['beer']
        logging.debug('Attempting to parse reviews for beer: ' + str(beer_item['beer_id']))
        soup = BeautifulSoup(response.body.decode('utf-8'), 'lxml')
        #reviews = soup.select('div[class*="checkin"]') 
        reviews = soup.findAll('div', {'class':'item'})
        logging.debug('Found {} reviews for beer: '.format(str(len(reviews))) + str(beer_item['beer_id']))
        for review in reviews:
            review_item = BeerReview()
            review_item['id'] = review['data-checkin-id']
            review_item['beer_id'] = beer_item['beer_id']
            user = review.find('a', {'class':'user'})
            if user:
                review_item['user_id'] = user['href'].split('/')[-1]
            comment = review.find('div', {'class':'checkin-comment'})
            if comment:
                text = comment.find('p', {'class':'comment-text'})
                if text:
                    review_item['text'] = text.text.strip()
                serving = comment.find('p', {'class':'serving'})
                if serving:
                    review_item['serving_type_id'] = serving.text.strip()
            rating = review.find('span', {'class':'rating'})
            if rating:
                rating_str = rating['class'][-1]
                review_item['rating'] = int(rating_str.replace('r', '')) / 100
            date = review.find('p', {'class':'time'})
            if date:
                review_item['created_dtm'] = parser.parse(date['data-gregtime']).strftime('%Y-%m-%d %H:%M:%S')   
            venue_link = review.find(lambda tag: tag.name == 'a' and '/v/' in tag['href'])
            if venue_link:
                review_item['id'] = venue_link['href'].split('/')[-1]
                yield Request(self.domain + venue_link['href'])
                
            yield review_item
            
        more_reviews = soup.find('a', {'class':'more_search'})
        if more_reviews:
             yield Request(self.search_url + 'search/more_search/beer?offset={}&q=beer&sort=all'.format(str(self.offset)),
                          callback=self.parse_beers)
             
    def parse_brewery(self, response):
        brewery_item = Brewery()
        soup = BeautifulSoup(response.body.decode('utf-8'), 'lxml')
        brewery_item['id'] = soup.find('p', {'class':'more'}).a['href'].split('/')[-2]
        content = soup.find('div', {'class':'content'})
        name = content.find('div', {'class':'name'})
        if name:
            brewery_item['name'] = name.h1.text.strip()
            brewery_item['style'] = name.find('p', {'class':'style'}).text.strip()
        description = soup.find('div', {'class':'beer-descrption-read-less'})
        if description:
            brewery_item['BreweryDescr'] = description.text.replace('Show Less', '').strip()
        date = soup.find('p', {'class':'date'})
        if date:          
            date_raw = date.text.strip()
            date_stripped = date_raw.replace('Added','').strip()
            date_parsed = parser.parse(date_stripped)
            brewery_item['BreweryCreatedDate'] = date_parsed.strftime('%Y-%m-%d')  
        beers = soup.find('p', {'class':'count'})
        brewery_locations = soup.find(text='Brewery Locations')
        if beers:
            yield Request(self.domain + beers.a['href'], callback=self.parse_beers_from_brewery, 
                          meta={'brewery':brewery_item})
        yield brewery_item

    def parse_brewery_locations(self, response, soup):
        brewery_item = response.meta['item']
        location = soup
        while True:
            brewery_location_item = BreweryLocation()
            brewery_location_item['brewery_id'] = brewery_item['id']
            location = location.find_next('div', {'class':'item'})
            


            
    def parse_beers_from_brewery(self, response):
        #Styles
        try:
            beer_styles = pandas.read_csv('BEER_STYLES.csv')
            unique_styles = list(set(beer_styles.name))
        except:
            unique_styles = []
        
        
        brewery_item = response.meta['brewery']
        brewery_id = brewery_item['BreweryId']
        soup = BeautifulSoup(response.body.decode('utf-8'), 'lxml')
        beers = soup.findAll('div', {'class':'beer-details'})
        for beer in beers:
            if brewery_id not in self.brewery_beer_counter:
                self.brewery_beer_counter[brewery_id] = 0
            self.brewery_beer_counter[brewery_id] += 1
            beer_item = Beer()
            beer_item['BreweryId'] = brewery_id
            name = beer.find('p', {'class':'name'})
            if name:
                beer_item['BeerName'] = name.a.text.strip()
                beer_item['BeerId'] = name.a['href'].split('/')[-1]
            style = beer.find('p', {'class':'style'})
            if style:
                beer_item['BeerStyle'] = style.text.strip()
                if beer_item['BeerStyle'] not in unique_styles:
                    unique_styles.append(beer_item['BeerStyle'])
            date = beer.find('p', {'class':'date'})
            if date:          
                date_raw = date.text.strip()
                date_stripped = date_raw.replace('Added','').strip()
                date_parsed = parser.parse(date_stripped)
                beer_item['BeerCreatedDate'] = date_parsed.strftime('%Y-%m-%d')  
            details = beer.find('div', {'class':'details'})
            if details:
                abv = details.find('p', {'class':'abv'})
                if abv:
                    beer_item['BeerABV'] = re.findall(r'\d+', abv.text)[0]
                ibu = details.find('p', {'class':'ibu'})
                if ibu:
                    beer_item['BeerIBU'] = re.findall(r'\d+', ibu.text)[0]
            description = beer.select('p[class*="desc-full"]')[0]
            if description:
                beer_item['BeerDescr'] = description.text.replace('Show Less', '').replace('Read Less', '').strip()
            beer_styles = pandas.DataFrame(unique_styles, columns=['name'])
            beer_styles.to_csv('BEER_STYLES.csv', index=False)
            yield beer_item
        
        more_beers = soup.find(text="Show More")
        if more_beers:            
            yield Request('https://untappd.com/brewery/more_beer/{}/{}?sort=most_popular'.format(
                    brewery_id,
                    str(self.brewery_beer_counter[brewery_id])),
                callback = self.parse_beers_from_brewery
                )
            
