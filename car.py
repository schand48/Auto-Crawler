#Author:Sumi
#car.py
# Class representing a Car

#import datetime #not used yet. will use for year and carDate

class Car:

    # Attributes of a Car
    # All variables are private
    def __init__(self):
        self.__name = ""
        self.__mileage = 0
        self.__dealer_name = ""
        self.__price = 0
        self.__year = 0
        self.__make = ""
        self.__model = ""
        self.__description = ""
        self.__carURL = ""
        self.__carDate = ""

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_dealer_name(self):
        return self.__dealer_name

    def set_dealer_name(self, dealer_name):
        self.__dealer_name = dealer_name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        assert year > 0
        self.__year = year

    def get_make(self):
        return self.__make

    def set_make(self, make):
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

    def get_carURL(self):
        return self.__carURL

    def set_carURL(self, carURL):
        self.__carURL = carURL

    def get_carDate(self):
        return self.__carDate

    def set_carURL(self, carDate):
        self.__carDate = carDate
