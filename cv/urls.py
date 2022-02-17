from django.urls import path
from . import views

app_name = 'cv'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page"),
    path('resume/', views.ResumeView.as_view(), name="resume_page"),
    path('resume-detial/<int:resume_id>/<slug:resume_slug>', views.ResumeDetialView.as_view(), name="resume_detial"),
    path('project/', views.ProjectView.as_view(), name="project_page"),
    path('project-detial/<int:project_id>/<slug:projects_slug>', views.ProjectDetialView.as_view(), name="project_detial"),
]
