from django.db import models
from authentication import custom_user

class UserLocation(models.Model):
    user = models.ForeignKey(custom_user.CustomUser, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
