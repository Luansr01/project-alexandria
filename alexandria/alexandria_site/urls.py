from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("home/", views.home, name = 'home'),
    path("", views.home, name = 'home'),

    path("about/", views.about, name = 'about'),
    path("projects/", views.projects, name='projects'),
    path("news/", views.news, name='news'),
    path("contact/", views.contact, name='contact'),

    path("<str:slug>", views.project, name='project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)