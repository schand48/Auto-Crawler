from bs4 import BeautifulSoup   
import requests 
import pandas as pd   

class Autotrader:
            
    data = []
    root_url = 'https://www.autotrader.com'

    for i in range (1,12):
        website = f'https://www.autotrader.com/cars-for-sale/all-cars/modesto-ca-95355?dma=&searchRadius=50&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords={i}'
        response = requests.get(website)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('div', {'data-cmp':'inventoryListing'})
        for result in results:
            data.append({
                    #Vehcile Name:
                    'name': result.find('h2').get_text() if result.find('h2') else None,
                    #Vehcile Price: 
                    'price': result.find('div', {'data-cmp':'pricing'}).get_text() if result.find('div',{'data-cmp':'pricing'}) else None,
                    #Vehicle Mileage:
                    'mileage':result.find('div', {'class':'item-card-specifications col-xs-9 margin-top-4 text-subdued-lighter'}).get_text() if result.find('div', {'class':'item-card-specifications col-xs-9 margin-top-4 text-subdued-lighter'}) else None,
                    #Dealer Name:
                    'dealer_name': result.find('div', {'data-cmp':'ownerDistance'}).get_text() if result.find('div',{'data-cmp':'ownerDistance'}) else None,
                    #Link to dealer:
                    'carURL': root_url + result.find('a', {'rel':'nofollow'}).get('href') if result.find('a', {'rel':'nofollow'}) else None
                })  
                
    #Export Data to excel file. 
    car_listings = pd.DataFrame(data)
    #car_listings.to_excel('cars/data/Autotrader.xlsx')
    car_listings.to_csv('cars/data/Autotrader_page1.csv')
        
    
        



