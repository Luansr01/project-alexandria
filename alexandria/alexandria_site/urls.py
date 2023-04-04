from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name = 'home'),
    path("", views.home, name = 'home'),
    path("home/old", views.home_old, name = 'home_old'),

    path("about/", views.about, name = 'about'),
    path("about_us/", views.about_us, name='about_us'),
    path("projects/", views.projects, name='projects'),
    path("news/", views.news, name='news'),
    path("contact/", views.contact, name='contact'),

    path("<str:slug>", views.project, name='project'),
]