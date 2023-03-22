from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name = 'home'),
    path("home/old", views.home_old, name = 'home_old'),
    path("about/", views.about, name = 'about'),
]