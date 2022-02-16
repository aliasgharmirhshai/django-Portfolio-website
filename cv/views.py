from importlib.resources import path
from urllib import request
from django import views
from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeView(View):
    template_name = 'cv/home.html'

    def get(self, request):
        return render(request, self.template_name)


class ResumeView(View):
    template_name = 'cv/resume.html'
    
    def get(self, request):
        return render(request, self.template_name)


class ResumeDetialView(View):
    template_name = 'cv/resume-detial.html'
    
    def get(self, request):
        return render(request, self.template_name)


class ProjectView(View):
    template_name = 'cv/project.html'
    
    def get(self, request):
        return render(request, self.template_name)


class ProjectDetialView(View):
    template_name = 'cv/project-detial.html'
    
    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'cv/contact.html'
    
    def get(self, request):
        return render(request, self.template_name)