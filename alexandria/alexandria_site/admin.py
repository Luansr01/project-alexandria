from django.contrib import admin
from  django.contrib.auth.models  import  Group
from . import models

# Register your models here.

@admin.register(models.Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ("name", "projects")

@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "projects")

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "ods")
# admin.site.register(models.Post) TODO

# Unregister your models here.
admin.site.unregister(Group)

# Changes to Admin Site.
admin.site.site_header = "Projeto Somar"
admin.site.site_title = "Administração Somar"
admin.site.index_title  =  "Somar | Administração"
admin.site.index_template = "alexandria_site/admin/changes.html"