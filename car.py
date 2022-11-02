#Author:Sumi
#car.py
# Class representing a Car
import csv 
#import datetime #not used yet. will use for year and carDate

class Car:

    # Attributes of a Car
    # All variables are private
    def __init__(self, number, name, mileage, price, carURL, dealer_name):
        self.__name = ""
        self.__mileage = 0
        self.__dealer_name = ""
        self.__price = 0
        self.__carURL = ""
        #self.__year = 0
        #self.__make = ""
        #self.__model = ""
        #self.__description = ""
        #self.__carDate = ""

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        self.__mileage = mileage
    
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_carURL(self):
        return self.__carURL

    def set_carURL(self, carURL):
        self.__carURL = carURL

    def get_dealer_name(self):
        return self.__dealer_name

    def set_dealer_name(self, dealer_name):
        self.__dealer_name = dealer_name



