from django.db import models
from django.urls import  reverse

# Create model gor booktype

class Cartype(models.Model):
    ctype = models.CharField(max_length=100, unique=True)
    class Meta:
        ordering=('ctype',)

class Car(models.Model):
    name = models.CharField(max_length=255)
    mileage = models.FloatField()
    price = models.FloatField()
    dealer_name = models.CharField(max_length=255)
    carURL = models.CharField(max_length=255)

#    def __str__(self):
#        return self.name
    class Meta:
        ordering=('name',)
    
    def __str__(self):
        return self.name
    
    def get_url(self):
       return reverse('car_detail', args=[self.id])