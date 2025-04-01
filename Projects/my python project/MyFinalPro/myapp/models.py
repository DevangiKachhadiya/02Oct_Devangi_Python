from django.db import models

# Create your models here.
class UserSignUp(models.Model):
    fnm = models.CharField(max_length=50)
    lnm = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    confpass = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    reset_pwd = models.CharField(max_length=10, blank=True, null=True)

class Owner(models.Model):
    STATUS_CHOICE = [
            ('Pending','Pending'),
            ('Approved','Approved'),
            ('Rejected','Rejected'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.BigIntegerField()
    is_approved = models.CharField(choices = STATUS_CHOICE, default= 'Pending', max_length=50)

class AddHome(models.Model):
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
    sprice = models.BigIntegerField(null=True, blank=True)
    rprice = models.BigIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, related_name='addhome_set')

class HomeImage(models.Model):
    home = models.ForeignKey(AddHome, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='house_imgs/')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneno = models.BigIntegerField()
    imessage = models.TextField() 

class reqtour(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=50)
    rtuemail=models.EmailField()
    contact = models.BigIntegerField()




