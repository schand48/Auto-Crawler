from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Car


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Car
    template_name = 'search_results.html'
