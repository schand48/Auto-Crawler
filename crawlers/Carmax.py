from bs4 import BeautifulSoup   
import requests 
import pandas as pd   

class CarMax:
            
    data = []
    root_url = 'https://www.carmax.com/'

    for i in range (1,12):
        website = f'https://www.carmax.com/cars/all'
        response = requests.get(website)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('div', {'class':'car-tile--content'})
        for result in results:
            data.append({
                    #Vehcile Year & Make:
                    'Vehicle Year & Make': result.find('span', {'class':'year-make'}).get_text() if result.find('span', {'class':'year-make'}) else None,
                    #Vehcile Model Trim: 
                    'Vehile Model & Trim': result.find('span', {'class':'model-trim'}).get_text() if result.find('div',{'data-cmp':'model-trim'}) else None,
                    #Vehicle Mileage:
                    'Vehicle Mileage':result.find('span', {'class':'miles'}).get_text() if result.find('span', {'class':'miles'}) else None,
                    #Link to dealer:
                    'Link to dealer': root_url + result.find('a', {'rel':'nofollow'}).get('href') if result.find('a', {'rel':'nofollow'}) else None
                })  
                
    #Export Data to excel file. 
    car_listings = pd.DataFrame(data)
    car_listings.to_excel('Carmax.xlsx')
        
    
        



