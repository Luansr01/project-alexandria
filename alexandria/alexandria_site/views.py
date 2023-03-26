from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import models


# Create your views here.

def home(request):
    return render(request, 'alexandria_site/home.html')

def about(request):
    return render(request, 'alexandria_site/about.html')

def about_us(request):
    return render(request, 'alexandria_site/about_us.html')   

def projects(request):
    objectives = models.Objective.objects.all()
    return render(request, 'alexandria_site/projects.html', {
        "objectives": objectives,
        "bgimg": "background-image: url('../static/leaves_tileable.jpg'); background-size: 600px; max-height=100%;",
        })   

def contact(request):
    return render(request, 'alexandria_site/contact.html')   

def home_old(request):
    return render(request, 'alexandria_site/home_old.html')        