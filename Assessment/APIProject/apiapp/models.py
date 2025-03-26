from django.db import models

# Create your models here.

class StudInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=20)
    
