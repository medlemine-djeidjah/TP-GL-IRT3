from django.db import models
from . import custom_user

# Create your models here.

class ServiceProvider(models.Model):
    user = models.OneToOneField(custom_user.CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    job = models.CharField(max_length=15 ,choices= {"Mechanic" : "Mechanic", "Electritien": "Electritien", "ShopOwner": "ShopOwner", "Other":"Other"})
    is_available = models.BooleanField(default=True)