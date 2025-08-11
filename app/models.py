from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_At = models.DateField(auto_now=True)
    isPublish = models.BooleanField(default=True)
