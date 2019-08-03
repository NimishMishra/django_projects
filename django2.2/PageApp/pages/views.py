from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView
# Create your views here.


# TemplateView already has all the language needed to display the template,
# we just need to write the template's name
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


# When based class based view, you always add as_view() to create the view.
# The regular exression '' is the default homepage
urlpatterns = [path('about/', AboutPageView.as_view(), name = 'about'),
               path('', HomePageView.as_view(), name = 'home'),
               
    ]