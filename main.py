import pandas as pd

df = pd.read_csv('cars/data/car_listings_page1.csv')

print(df.to_string())