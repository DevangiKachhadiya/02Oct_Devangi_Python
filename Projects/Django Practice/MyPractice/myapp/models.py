from django.db import models


# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=20)
    emp_id=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)
    

