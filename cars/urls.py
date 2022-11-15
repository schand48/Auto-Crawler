#Author: Sumi
# cars/urls.py
from django.urls import path
from .views import HomePageView, SearchResultsView
#from cars import views


urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
]