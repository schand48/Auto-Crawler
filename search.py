#Created by Sumi
from listing import Listing

class Search:
    def __init__(self):
        self.__car_listings = []

    def create_inventory(self, car_listings_page4):
        with open("car_listings_page4.csv", "r") as csvfile:
          csvreader = csv.reader(csvfile)
          for line in csvreader:

            car_data = Car()
            car_data.set_car_name(int(line[0]))
            car_data.set_mileage(line[1])
            car_data.set_price(line[2])
            car_data.set_dealer_name(line[3])
            car_data.set_listingURL(line[4])
        self.__car_listings.append(car_data)
