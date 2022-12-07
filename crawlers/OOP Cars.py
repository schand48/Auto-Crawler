# Written by: Luan
# Tested by: Sumi
# Debugged by: Luan
#One of the main crawlers - however not in Object oriented format
from bs4 import BeautifulSoup   
import requests 
import pandas as pd
import csv
import urllib.parse 

data = []
root_url = 'http://www.cars.com'

def getdata(page):

        #Give Bs4 a source
        
        website= f'https://www.cars.com/shopping/results/?page={i}&page_size=20&dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip=95355'
        #Requesting using requests lib 
        response = requests.get(website)
        soup = BeautifulSoup(response.content, 'html.parser')
        #Finding results 
        results = soup.find_all('div', {'class':'vehicle-card'})
        for result in results:
            data.append({
                #Vehicle Name
                'Vehicle Name': result.find('h2').get_text() if result.find('h2') else None,
                #Vehicle Price
                'Price':result.find('span', {'class':'primary-price'}).get_text() if result.find('span', {'class':'primary-price'}) else None,
                #Vehicle Mileage
                'Mileage':result.find('div', {'class':'mileage'}).get_text() if result.find('div', {'class':'mileage'}) else None,
                #Dealer Name
                'Dealer Name':result.find('div', {'class':'dealer-name'}).get_text() if result.find('div',{'class':'dealer-name'}) else None, 
                #Link 
                'Link': root_url+result.find('a', {'class':'vehicle-card-visited-tracking-link'}).get('href') if result.find('a', {'class':'vehicle-card-visited-tracking-link'}) else None
                })
        return

for i in range(1,12):
    getdata(i)

carlisting = pd.DataFrame([data])
carlisting.to_excel('Test4.xlsx')