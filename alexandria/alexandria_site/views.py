from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import models


# Create your views here.

def home(request):
    return render(request, 'alexandria_site/home.html', {"title": "Página Inicial"})

def about(request):
    return render(request, 'alexandria_site/about.html')

def about_us(request):
    return render(request, 'alexandria_site/about_us.html')   

def projects(request):
    objectives = models.Objective.objects.all()
    projects = models.Project.objects.all()
    return render(request, 'alexandria_site/projects.html', {
        "objectives": objectives,
        "projects": projects,
        "bgimg": "background-image: url('../static/leaves_tileable.jpg'); background-size: 50%; max-height=100%;",
        })   

def news(request):
    posts = reversed(models.Post.objects.all())
    return render(request, 'alexandria_site/news.html', {
        "posts": posts,
        "bgimg": "background-color: var(--lighter);"

    })

def contact(request):
    return render(request, 'alexandria_site/contact.html')   

def project(request, slug):
    
    sl = models.Project.objects.get(slug=slug)
    ods = ", ".join(list(map(lambda n : n.name, list(sl.ODS.all())))) #Gets all of the names of the ODSs associated with the project and concatenates them into a string separated by a comma.
    partners = list(sl.partners.all())

    if (sl.image_1 or sl.image_2 or sl.image_3):
        images = [sl.image_1, sl.image_2, sl.image_3]
    else:
        images = False

    return render(request, 'alexandria_site/project_page.html', {"project":sl, "ods":ods, "partners":partners, "images":images, "value":range(5000)})