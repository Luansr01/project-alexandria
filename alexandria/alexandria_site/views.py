from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def home(request):
    return render(request, 'alexandria_site/home.html')

def about(request):
    return render(request, 'alexandria_site/about.html')

def home_old(request):
    return render(request, 'alexandria_site/home_old.html')        