#Author: Sumi
import csv
from car import Car

class Search(Car):
    def __init__(self):
        self.__car_list = []

    def create_database(self, car_listings_page4):
        car_list = []
        with open('cars/static/car_listings_page4.csv', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # Skip the header.
            # Unpack row directly 
            for number, name, mileage, price, carURL, dealer_name in reader:
                # create instance and append it to the list.
                car_list.append(Car(number, name, mileage, price, carURL, dealer_name))
    
    def search_keyword(self, name):
        for car in self.__car_list:
            if car.get_name().lower() == name.lower(): 
                return car 
        return None

#testing search class
if __name__ == "__main__":
    cDatabase = Search()
    cDatabase.create_database("/static/car_listings_page4.csv")
   # print(cDatabase)
    keyword = input("Enter car name: ")
    searchKeyword = cDatabase.search_keyword(keyword)[0]

    if searchKeyword == []:
        print( f"\n{keyword} is not in the data.")
    else:
        print(searchKeyword.get_name()+ "Mileage:" + searchKeyword.get_mileage())