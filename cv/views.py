from django.shortcuts import render
from django.views import View
from .models import ResumeDetial, ProjectDetial
# Create your views here.


class HomeView(View):
    template_name = 'cv/home.html'

    def get(self, request):
        return render(request, self.template_name)


class ResumeView(View):
    template_name = 'cv/resume.html'

    def get(self, request):
        resume = ResumeDetial.objects.all()
        return render(request, self.template_name, {'resume':resume})


class ResumeDetialView(View):
    template_name = 'cv/resume-detial.html'
    
    def get(self, request):
        return render(request, self.template_name)


class ProjectView(View):
    template_name = 'cv/project.html'
    
    def get(self, request):
        project = ProjectDetial.objects.all()
        return render(request, self.template_name, {'project':project})


class ProjectDetialView(View):
    template_name = 'cv/project-detial.html'
    
    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'cv/contact.html'
    
    def get(self, request):
        return render(request, self.template_name)