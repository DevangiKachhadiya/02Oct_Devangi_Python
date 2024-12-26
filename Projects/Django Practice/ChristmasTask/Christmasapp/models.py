from django.db import models

# Create your models here.
class Santa(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=10)
    address=models.TextField()
    city=models.CharField(max_length=10)

class Login(models.Model):
   first_name=models.CharField(max_length=10)
   last_name=models.CharField(max_length=10)
   email=models.EmailField()
   password=models.CharField(max_length=10)
   
   