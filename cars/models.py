from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    mileage = models.FloatField()
    price = models.FloatField()
    dealer_name = models.CharField(max_length=255)
    carURL = models.CharField(max_length=255)

    def __str__(self):
        return self.name