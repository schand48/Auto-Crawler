#Author: Luan Vo
#from grp import struct_group
from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.parse

name = []
price = []
mileage = []
dealer_name =[]
source = []

for i in range (1,13):
        #Allow to Crawl multiple pages:
        website ='https://www.cars.com/shopping/results/?page=' + str(i) + '&page_size=20&dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip=95355'
        #Requesting using requests lib
        response = requests.get(website)

        soup = BeautifulSoup(response.content, 'html.parser')
        #Finding results
        results = soup.find_all('div', {'class':'vehicle-card'})

        for result in results:
            # name
            try:
                name.append(result.find('h2').get_text())
            except:
                name.append('n/a')
            #price
            try:
                price.append(result.find('span', {'class':'primary-price'}).get_text())
            except:
                price.append('n/a')

            # mileage
            try:
                mileage.append(result.find('div', {'class':'mileage'}).get_text())
            except:
                mileage.append('n/a')
            # dealer_name
            try:
                dealer_name.append(result.find('div', {'class':'dealer-name'}).get_text().strip())
            except:
                dealer_name.append('n/a')
            #link
            try:
                source.append(result.find('a', {'class':'vehicle-card-visited-tracking-link'}).get('href'))
            except:
                source.append('n/a')

#Using Pandas to create a dictionary and import to Excel
car_listings = pd.DataFrame({'Name': name, 'Mileage':mileage, 'Price': price, 'Dealer Name':dealer_name,'Link': source})
car_listings.to_excel('car_listings_page4.xlsx')
