from bs4 import BeautifulSoup   
import requests 
import pandas as pd   
from time import time, sleep 
from random import randint



class Crawler:
    data = []
    root_url = 'http://www.cars.com'
    page = [str(i) for i in range (1,10)]
    zip = [str(i) for i in range (90001,96162)]
    request = 0 
    start_time = time()
    for pages in page:
        for zipcode in zip:
            website= f'https://www.cars.com/shopping/results/?page={page}&page_size=20&dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip={zip}' 
            sleep(randint(8,15))
            request +=1
            elapsed_time = time() - start_time
        if request > 40:
            break
        

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
                
    #Export Data to excel file. 
    car_listings = pd.DataFrame(data)
    car_listings.to_excel('car_listings_page2.xlsx')
        



        
            

