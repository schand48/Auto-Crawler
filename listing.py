# listing.py
# Class representing a Listing

import datetime #not used yet. will use for year and listingDate

class Listing:

    # Attributes of a Listing
    # All variables are private
    def __init__(self):
        self.__year = 0
        self.__make = ""
        self.__model = ""
        self.__price = 0
        self.__description = ""
        self.__listingURL = ""
	self.__listingDate = ""
 
    # Getters and Setters
    def get_year(self):
        return self.__year

    def set_year(self, year):
        assert year > 0  
        self.__year = year

    def get_make(self):
        return self.__make

    def set_make(self, make)
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_listingURL(self):
        return self.__listingURL

    def set_listingURL(self, listingURL):
        self.__listingURL = listingURL

    def get_listingDate(self):
        return self.__listingDate

    def set_listingURL(self, listingDate):
        self.__listingDate = listingDate