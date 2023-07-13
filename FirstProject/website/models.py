from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    Age = models.IntegerField(max_length=5)
    roll_no = models.IntegerField(max_length=10)
    address  = models.CharField(max_length=1000)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    salary = models.IntegerField(max_length=10)
    address  = models.CharField(max_length=1000) 