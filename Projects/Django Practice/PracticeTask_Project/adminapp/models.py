from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='product_images/')