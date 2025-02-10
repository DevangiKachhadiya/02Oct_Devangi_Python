from django.db import models

class Usersignup(models.Model):
    role=models.CharField(max_length=20)
    firstname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    contact=models.BigIntegerField()


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

#Doctor Model
class Doctors(models.Model):
    img = models.ImageField(upload_to='doctimg')
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    address = models.TextField()
    created=models.DateTimeField(auto_now_add=True)

#Patient Models
class Patient(models.Model):
    email = models.EmailField()
    age = models.IntegerField()
    Contact = models.BigIntegerField()

#Appoinment Model
class Appoi(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    contact = models.BigIntegerField()
    dt = models.DateTimeField()