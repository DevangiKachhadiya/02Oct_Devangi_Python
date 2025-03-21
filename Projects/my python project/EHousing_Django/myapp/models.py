from django.db import models

# Create your models here.
class userSignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fn = models.CharField(max_length=50)
    ln = models.CharField(max_length=50)
    email = models.EmailField()
    pas = models.CharField(max_length=12)
    cpas = models.CharField(max_length=12)

class addhome(models.Model):
    HOME_TYPE_CHOICES = [
        ('rent', 'Rent'),    
        ('sell', 'Sell'),
    ]

    hname = models.CharField(max_length=100)
    address = models.TextField()    
    city = models.CharField(max_length=100)
    size = models.FloatField()
    bedroom = models.IntegerField()
    desc = models.TextField()
    htype = models.CharField(max_length=10, choices=HOME_TYPE_CHOICES)
    price = models.BigIntegerField(null=True, blank=True)
    rprice = models.BigIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class HomeImage(models.Model):
    home = models.ForeignKey(addhome, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='house_imgs/')
