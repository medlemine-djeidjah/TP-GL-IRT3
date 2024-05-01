from django.contrib.auth.models import AbstractUser

from django.db import models


class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('service_provider', 'Service Provider'),
        ('client', 'Client'),
    )
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='client')

    def save(self, *args, **kwargs):
        # Call set_password to hash the password before saving
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)
