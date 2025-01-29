from django.db import models

class permissionroles(models.Model):
    ROLE_CHOICES ={
        (1,'patients'),
        (2,'doctor'),
        }
    user_type = models.CharField(choices=ROLE_CHOICES,max_length=50,default=1)

    profile_pic = models.ImageField(upload_to='media/profile_pic')


class signup(models.Model):
    ROLE_CHOICES = [
        ('1', 'Doctor'),
        ('2', 'Patient'),
        ('3', 'Admin'),
    ]
    role=models.CharField(max_length=20, choices=ROLE_CHOICES)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact=models.BigIntegerField()


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

