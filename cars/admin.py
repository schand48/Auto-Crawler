# Written by: Sumi
# Tested by:
# Debugged by:

from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "mileage","dealer_name","carURL")

admin.site.register(Car, CarAdmin)