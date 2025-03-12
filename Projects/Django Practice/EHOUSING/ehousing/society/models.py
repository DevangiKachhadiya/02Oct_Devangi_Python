from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('user', 'User'),
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users_permissions',  # Unique related name
        blank=True
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class Society(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()

    def __str__(self):
        return self.name

class House(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=50)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    is_rented = models.BooleanField(default=False)
    is_for_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.house_number} - {self.society.name}"

class Complaint(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Owner(AbstractUser):  # Owner is a User with extra details
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    is_first_login = models.BooleanField(default=True)  # Forces password change

    # Fix reverse accessor clash by renaming the related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='owner_users',  # Change related_name to something unique
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='owner_users_permissions',  # Change related_name
        blank=True
    )

class Home(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)  # Links home to owner
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)  # Home available or not
    created_at = models.DateTimeField(auto_now_add=True)
