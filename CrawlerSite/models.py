#Created by Richard
#Updated by Sumi

# Import necessary modules
from django.db import models
from django.urls import  reverse


#Create model for cartype
class Cartype(models.Model):
    ctype = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering=('ctype',)

# Create model for Car
class Car(models.Model):
    car_name = models.CharField(max_length=150)
    mileage = models.FloatField(max_length=150)
#    type = models.ForeignKey(cartype, on_delete=models.CASCADE)
    price = models.FloatField()
    dealer_name = models.CharField(max_length=100)

    class Meta:
        ordering=('car_name',)
#
    def __str__(self):
        return self.car_name

    def get_url(self):
       return reverse('car_detail', args=[self.id])
