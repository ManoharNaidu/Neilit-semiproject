from django.db import models

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=1000)
    origin = models.CharField(max_length=1000)
    destination = models.CharField(max_length=1000)
    date = models.DateField()
