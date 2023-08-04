from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from random import randint

from . import models
from . import forms


# Views

def home(request):
    return render(request, 'alexandria_site/home.html', {"title": "Página Inicial"})

def about(request):
    return render(request, 'alexandria_site/about.html', {"title": "Sobre"})

def projects(request):
    def most_common(lst):
        return max(set(lst), key=lst.count)

    objectives = models.Objective.objects.all()
    projects = models.Project.objects

    states = [(x[1], list(projects.filter(state=x[0]))) for x in models.STATE_CHOICES]
    #cities = [(f'{most_common(list(projects.filter(city=x["city"]).values_list("state", flat=True)))} - {x["city"]}', list(projects.filter(city=x['city']))) for x in projects.exclude(city=None).values('city').distinct()]
    cities = [(x[1], list(projects.filter(city=x[0]))) for x in models.CITY_CHOICES]
    causes = [(x['cause'], list(projects.filter(cause=x['cause']))) for x in projects.exclude(cause=None).exclude(cause="").values('cause').distinct()]

    if request.method == "POST":
        form = forms.Filter(request.POST)
        if form.is_valid():
                return HttpResponseRedirect("#")
    else:
        form = forms.Filter()


    form.fields['filter'].initial = request.GET.get('filter', 'ods')
    return render(request, 'alexandria_site/projects.html', {
        "objectives": objectives,
        "projects": projects.all(),
        "bgimg": "background-image: url('../static/leaves_tileable.jpg'); background-size: 50%; max-height=100%;",
        "form":form,
        "filter":request.GET.get('filter', 'ods'),
        "causas":causes,
        "cidades":cities,
        "title": "Projetos"
        })   

def news(request):
    posts = reversed(models.Post.objects.all())
    return render(request, 'alexandria_site/news.html', {
        "posts": posts,
        "bgimg": "background-color: var(--lighter);"

    })

def contact(request):
    return render(request, 'alexandria_site/contact.html', {"title": "Contato"})   

def project(request, slug):
    
    sl = models.Project.objects.get(slug=slug)
    ods = ", ".join(list(map(lambda n : n.name, list(sl.ODS.all())))) #Gets all of the names of the ODSs associated with the project and concatenates them into a string separated by a comma.
    partners = list(sl.partners.all())

    if (sl.image_1 or sl.image_2 or sl.image_3 or sl.image_4 or sl.image_5 or sl.image_6):
        images = [sl.image_1, sl.image_2, sl.image_3, sl.image_4, sl.image_5, sl.image_6]
    else:
        images = False

    if (sl.video):
        video = sl.video.url
    else:
        video = False


    return render(request, 'alexandria_site/project_page.html', {"project":sl, "ods":ods, "partners":partners, "images":images, "video":video, "title": sl.name})