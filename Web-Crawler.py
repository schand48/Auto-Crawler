#Author: Luan 
from bs4 import BeautifulSoup   
import requests 
import pandas as pd
import csv
import urllib.parse 

class Crawler:
    data = []
    root_url = 'http://www.cars.com'

    for i in range (1,13):
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
                
    #Export Data to excel and .csv file and save in /static
    car_listings = pd.DataFrame(data)
    car_listings.to_excel('cars/data/car_listings_page1.xlsx')
    car_listings.to_csv('cars/data/car_listings_page1.csv') #Bug: csv formatting issues
    #car_listings.to_json('cars/data/car_listings_page1.json')