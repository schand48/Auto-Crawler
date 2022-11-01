#Created by Sumi
import csv
from car import Car

class Search:
    def __init__(self):
        self.__car_listings = []

    def create_database(self, car_listings_page4):
        with open("car_listings_page4.csv", "r") as csvfile:
          csvreader = csv.reader(csvfile)
          for line in csvreader:

            car_data = Car()
            car_data.set_name(line[1])
            car_data.set_mileage(line[2])
            car_data.set_price(line[3])
            car_data.set_dealer_name(line[4])
            car_data.set_carURL(line[5])
        self.__car_listings.append(car_data)
    
    def search_keyword(self, name):
        for car in self.__car_listings:
            if car.get_name().lower() == name.lower(): 
                return car 
        return None


#testing search class
if __name__ == "__main__":
    cDatabase = Search()
    cDatabase.create_database("car_listings_page4.csv")
    keyword = input("Enter car name: ")
    searchKeyword = cDatabase.search_keyword(keyword)[0]

    if searchKeyword == []:
        print( f"\n{keyword} is not in the data.")
    else:
        print("\nName:", str(searchKeyword.get_name()))
        print("Mileage:", searchKeyword.get_mileage())