from django.db import models
from adminapp.models import * 

# Create your models here.

class UserSignUp(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=12)

s= [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')]

class ReqProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'product_images/')
    user = models.ForeignKey(UserSignUp, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField( choices=s, max_length=50, default='pending')
