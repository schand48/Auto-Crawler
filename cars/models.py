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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dealer_name = models.CharField(max_length=255)
    carURL = models.CharField(max_length=255)

    class Meta:
        db_table = 'store_car'
        indexes = [
            models.Index(fields=['name', 'mileage', 'price', 'dealer_name', 'carURL' ])
            ]


    def __str__(self):
        return self.name
    
    # def get_url(self):
    #    return reverse('car_detail', args=[self.id])