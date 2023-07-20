from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Objective)
admin.site.register(models.Partner)
admin.site.register(models.Project)
# admin.site.register(models.Post) TODO