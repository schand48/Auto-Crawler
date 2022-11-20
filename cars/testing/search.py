# Written by: Sumi
# Tested by:
# Debugged by:
# Used for testing

import csv
import pandas as pd
from car import Car

class Search():
    def __init__(self):
        self.__car_list = []

    def create_csv_database(self, car_listings_page1):
        #convert excel to csv
        #df = pd.DataFrame(pd.read_excel("cars/data/car_listings_page1.xlsx"))
        #df.to_csv ("cars/data/car_listings.csv", index = None, header=True)

        with open("cars/data/car_listings_page4.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                car_data = Car()        
                #car_data.set_car_number(int(line[0]))
                car_data.set_name(line[1])
                car_data.set_price(line[2])
                car_data.set_mileage(line[3])
                car_data.set_dealer_name(line[4])
                car_data.set_carURL(line[5])
                self.__car_list.append(car_data)

    def search_keyword(self, name):
        for car in self.__car_list:
            if car.get_name().lower() == name.lower(): 
                return car 
        #return None

#testing search class
if __name__ == "__main__":
    cDatabase = Search()
    cDatabase.create_csv_database("cars/data/car_listings.csv")
   # print(cDatabase)
    keyword = "2022 Mitsubishi Outlander SE"
    searchKeyword = cDatabase.search_keyword(keyword)
    searchKeyword = cDatabase.search_keyword(keyword)

    if searchKeyword == []:
        print( f"\n{keyword} is not in the data.")
    else:
        print(searchKeyword.get_name()+ "Mileage:" + searchKeyword.get_mileage())