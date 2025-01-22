from django.db import models

# Create your models here.

class Appointment(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    appointdate=models.DateField()
    opt=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    message=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

class DoctorProfile(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    opt=models.CharField(max_length=100)
    city=models.CharField(max_length=300)
    mobile=models.BigIntegerField()
    username=models.EmailField()
    password=models.CharField(max_length=12)
    created=models.DateTimeField(auto_now_add=True)

class registeration(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    created=models.DateTimeField(auto_now_add=True)
