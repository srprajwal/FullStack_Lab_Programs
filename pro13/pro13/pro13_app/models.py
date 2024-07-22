from django.db import models
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default='')
    courses = models.ManyToManyField(Course, blank=True)