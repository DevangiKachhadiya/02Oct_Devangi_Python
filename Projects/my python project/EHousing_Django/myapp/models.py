from django.db import models

# Create your models here.
class userSignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fn = models.CharField(max_length=50)
    ln = models.CharField(max_length=50)
    email = models.EmailField()
    pas = models.CharField(max_length=12)
    cpas = models.CharField(max_length=12)
