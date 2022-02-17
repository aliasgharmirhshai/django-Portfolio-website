from django.urls import path
from . import views

app_name = 'cv'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home-page"),
    path('resume/', views.ResumeView.as_view(), name="resume-page"),
    path('resume-detial/', views.ResumeDetialView.as_view(), name="resume-detial"),
    path('project/', views.ProjectView.as_view(), name="project-page"),
    path('project-detial/', views.ProjectDetialView.as_view(), name="project-detial"),
    path('contact-me/', views.ContactView.as_view(), name="contact-page"),
]
