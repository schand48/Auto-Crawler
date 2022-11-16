#Author: Sumi
from django.db import models
from django.urls import  reverse

# Create model for cartype
# class Cartype(models.Model):
#     ctype = models.CharField(max_length=100, unique=True)
#     class Meta:
#         ordering=('ctype',)

# Create model for car
class Car(models.Model):
    name = models.CharField(max_length=255)
    mileage = models.FloatField()
    price = models.FloatField()
    dealer_name = models.CharField(max_length=255)
    carURL = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_url(self):
       return reverse('car_detail', args=[self.id])