from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    contact = models.BigIntegerField()

    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions_set", blank=True)

    # Society Model
class Society(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name

# House Model        
class House(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name="houses")
    house_number = models.CharField(max_length=10)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return f"{self.house_number} - {self.society.name}"

# Complaint Model
class Complaint(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints")
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="house_complaints")
    issue = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'),('resolved','Resolved')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.member.username} - {self.status}"
    
# Rental & Sale Listing Model
class HouseListing(models.Model):
    LISTING_TYPE = [
        ('rent', 'Rent'),
        ('sale', 'Sale'),
    ]
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="listings")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE)
    price = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.house} - {self.listing_type} - {self.price}"
    

# Message Model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"
    
