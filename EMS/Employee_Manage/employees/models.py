from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_ID = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=150)
    Address = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=10)
    
