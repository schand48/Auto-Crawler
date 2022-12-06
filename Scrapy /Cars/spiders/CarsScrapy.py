import scrapy 
import requests 
import pandas as pd
import csv

class Cars(scrapy.Spider):
    data = []
    name = 'Cars'
    start_urls = ['https://www.cars.com/shopping/results/?page=&page_size=20&dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip=95355']
    def parse(self, reponse):
        for results in reponse.css('div.vehicle-card'):
            yield {
                    'Vehicle Name': results.css('h2::text').get(),
                    'Price': results.css('span.primary-price::text').get(),
                    'Mileage': results.css('div.mileage::text').get(),
                    'Dealer Name': results.css('div.vehicle-dealer:text').get(),
                    'Link': results.css('a.vehicle-card-visited-tracking-link').attrib['href'],
                }
