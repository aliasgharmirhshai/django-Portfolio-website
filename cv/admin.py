from re import search
from django.contrib import admin
from .models import ResumeDetial, ProjectDetial
# Register your models here.

@admin.register(ResumeDetial)
class ResumeDetialAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'level', 'slug',)
    search_fields = ('company_name','description',)


@admin.register(ProjectDetial)
class ProjectDetialAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'slug',)
    search_fields = ('project_name','project_description',)