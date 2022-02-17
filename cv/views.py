from django.shortcuts import render, get_object_or_404
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
    
    def get(self, request, resume_id, resume_slug):
        resumes = ResumeDetial.objects.get(pk=resume_id, slug=resume_slug)
        return render(request, self.template_name, {'resumes':resumes})


class ProjectView(View):
    template_name = 'cv/project.html'
    
    def get(self, request):
        project = ProjectDetial.objects.all()
        return render(request, self.template_name, {'project':project})


class ProjectDetialView(View):
    template_name = 'cv/project-detial.html'
    
    def get(self, request, project_id, projects_slug):
        projects = ProjectDetial.objects.get(pk=project_id, slug=projects_slug)
        return render(request, self.template_name, {"projects":projects})


class ContactView(View):
    template_name = 'cv/contact.html'
    
    def get(self, request):
        return render(request, self.template_name)