from django.db import models

# Create your models here.

class usersignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    pwd = models.CharField(max_length=20)
    cpwd = models.CharField(max_length=20)
    contact = models.BigIntegerField()

class contactUs(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class house(models.Model):
    PROPERTY_TYPES = [
        ('Apartment', 'Apartment'),
        ('Villa', 'Villa'),
        ('Bungalow', 'Bungalow'),
        ('RowHouse', 'Rowhouse'),
    ]

    LISTING_TYPES = [
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
    ]

    title = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices = PROPERTY_TYPES)
    listing_type = models.CharField(max_length=10, choices = LISTING_TYPES)
    price = models.BigIntegerField()
    address = models.TextField()
    area = models.PositiveIntegerField(help_text="Size in square feet")
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    floors = models.PositiveIntegerField()
    main_image = models.ImageField(upload_to='house_images/')
    created = models.DateTimeField(auto_now_add=True)


class HouseImage(models.Model):
    house = models.ForeignKey(house, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='house_images/')

class complaints(models.Model):
    houseid = models.IntegerField()
    ComplaintsText = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
