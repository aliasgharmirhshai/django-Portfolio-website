from django.urls import path
from . import views

app_name = 'cv'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page"),
    path('resume/', views.ResumeView.as_view(), name="resume_page"),
    path('resume_detial/>', views.ResumeDetialView.as_view(), name="resume_detial"),
    path('project/>', views.ProjectView.as_view(), name="project"),
    path('project_detial/>', views.ProjectDetialView.as_view(), name="project-detial"),
    path('contact_me/>', views.ContactView.as_view(), name="contact_page"),
]
