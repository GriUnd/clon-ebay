from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    teacher = models.CharField(max_length=150)