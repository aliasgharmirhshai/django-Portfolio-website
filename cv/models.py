from turtle import Turtle
from django.db import models

# Create your models here.

class ResumeDetial(models.Model):
    company_name = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.company_name


class ProjectDetial(models.Model):
    project_name = models.CharField(max_length=30, null=True)
    project_description = models.TextField(null=True)
    project_slug = models.SlugField(max_length=250, null=True)
    project_image = models.ImageField(upload_to='img',null=True)
    project_url = models.URLField(max_length=200,  null=True)

    def __str__(self):
        return self.project_name