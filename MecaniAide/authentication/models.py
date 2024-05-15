from django.db import models
from . import custom_user

# Create your models here.

class ServiceProvider(models.Model):
    user = models.OneToOneField(custom_user.CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)

    # Define a list of tuples for job choices
    JOB_CHOICES = [
        ("Mechanic", "Mechanic"),
        ("Electrician", "Electrician"),  # Corrected spelling
        ("ShopOwner", "Shop Owner"),
        ("Other", "Other"),
    ]

    job = models.CharField(max_length=15, choices=JOB_CHOICES)
    is_available = models.BooleanField(default=True)
