from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
# Create your views here.

def homePageView(request):
    return HttpResponse('Hello world')


# If the user requests the home pages (represented by the empty 
#string), we use the view homePageView
# 
urlpatterns = [path('', homePageView, name = 'home')]