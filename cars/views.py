from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Car, Cartype
from django.db.models import Q
import csv
#from car import Car

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Car
    template_name = 'search_results.html'

# Define function to display all cars
def car_list(request):
    car = Car.objects.all()
    return render(request, 'car_list.html', {'car': car })

# Define function to display all cars

def car_list(request):
    car = Car.objects.all()
    return render(request, 'car_list.html', {'car': car })

# Define function to display the particular car
def car_detail(request,id):
    car = get_object_or_404(Car, id=id)
    types = Cartype.objects.all()
    t = types.get(id=car.type.id)
    return render(request, 'car_detail.html', {'car': car, 'type': t.ctype})


# Define function to search car
def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Car.objects.filter(Q(name__icontains=query) | Q(mileage__icontains=query) | Q(price__icontains=query) | Q(dealer_name__icontains=query) )
    return render(request, 'search.html', {'query': query, 'results': results})

def index(request):
    car = {'name':'b', 'mileage':'c', 'price': 'd', 'dealer_name':'e','carURL': 'f'}
    file = open("/static/car_listings_page4.csv")
    csvreader = csv.reader(file)
    rows = []
    d = dict()
    for row in csvreader:
       rows.append(row)

    return render(request, 'home.html',car)

