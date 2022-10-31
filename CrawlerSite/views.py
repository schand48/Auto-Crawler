#Created by Richard
#Updated by Sumi
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import  Car

from django.db.models import Q
from .models import Car

def car_detail(request,id):
    car = get_object_or_404(Car, id=id)
    types = Cartype.objects.all()
    t = types.get(id=car.type.id)
    return render(request, 'car_detail.html', {'car': car, 'type': t.ctype})

#class HomePageView(TemplateView):
#    template_name = 'home.html'

#class SearchResultsView(ListView):
#    model = Car
#    template_name = 'search_results.html'

#def index(request):
#    return HttpResponse("This is the start of the Auto Crawler project site.")
