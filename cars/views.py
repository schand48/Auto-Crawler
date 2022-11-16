#Author: Sumi
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Car

# Used for testing
# Defining function to display all cars
# def car_list(request):
#     car = Car.objects.all()
#     return render(request, 'car_list.html', {'car': car })

#Class for Homepage
class HomePageView(TemplateView):
    template_name = 'home.html'
#Class for Search Results
class SearchResultsView(ListView):
    model = Car
    template_name = 'search_results.html'

# function for searchbar to search through user query
def search(request):
    try:
        queryset = Car.objects.filter(name__icontains='Lexus')
        return render(request, 'search.html', {'car': list(queryset)})
    except ObjectDoesNotExist:
        pass
    
    
    # #load csv data
    # with open("cars/data/car_listings_page4.csv", "r") as csvfile:
    #     csvreader = csv.reader(csvfile)
    #     for line in csvreader:
    #         _, created = Car.objects.get_or_create(
    #             number=line[0],
    #             name=line[1],
    #             mileage=line[2],
    #             price=line[3],
    #             name=line[4],
    #             carURL=line[5]
    #             )
    # results = []
    # if request.method == "GET":
    #     query = request.GET.get('search')
    #     if query == '':
    #         query = 'None'
    #     results = Car.objects.filter(Q(name__icontains=query))
    # return render(request, 'search.html', {'query': query, 'results': results})


# # # Define function to display the particular car
#     def car_detail(request,id):
#         car = get_object_or_404(Car, id=id)
#         types = Cartype.objects.all()
#         t = types.get(id=car.type.id)
#         return render(request, 'car_detail.html', {'car': car, 'type': t.ctype})

# # Define function to search car
# def search(request):
#     #form = SearchForm()
#     results = []
#     if request.method == "GET":
#         query = request.GET.get('search')
#         if query == '':
#             query = 'None'
#         results = Car.objects.filter(Q(name__icontains=query) | Q(mileage__icontains=query) | Q(price__icontains=query) | Q(dealer_name__icontains=query) )
#     return render(request, 'search.html', {'query': query, 'results': results})

# def index(request):
#     car = {'name':car.name, 'mileage':car.mileage, 'price': car.price, 'dealer_name': car.dealer_name,'carURL': car.carURL}
#     file = open("/static/car_listings_page4.csv")
#     csvreader = csv.reader(file)
#     rows = []
#     d = dict()
#     for row in csvreader:
#        rows.append(row)
#     for r in rows:
#        d.update({r[0]:r[1]})
#        print(r[0]) 
#     return render(request, 'home.html',car)

