from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Choix pour le type de service
SERVICE_CHOICES = [
    ('towing', 'Towing'),
    ('flat_battery', 'Flat Battery'),
    ('fuel_delivery', 'Fuel Delivery'),
    ('lost_key', 'Lost Key'),
    ('flat_tire', 'Flat Tire'),
    ('diagnostic', 'Diagnostic'),
]

# Choix pour le type de paiement
PAYMENT_METHOD_CHOICES = [
    ('cash', 'Cash'),
    ('bankily', 'bankily'),
    ('masrvi', 'Masrvi'),
]

# Choix pour le type de carburant
FUEL_TYPE_CHOICES = [
    ('gasoline', 'Gasoline'),
    ('diesel', 'Diesel'),
]

# Choix pour le type de technicien
TECHNICIAN_TYPE_CHOICES = [
    ('mechanic', 'Mechanic'),
    ('electrician', 'Electrician'),
]

class ServiceRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Association avec l'utilisateur
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField(blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    video = models.FileField(upload_to='service_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Spécificités de chaque service
    litres = models.FloatField(blank=True, null=True)  # Pour Fuel Delivery
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES, blank=True, null=True)  # Gazoil ou Essence
    car_brand = models.CharField(max_length=50, blank=True, null=True)  # Pour Lost Key
    technician_type = models.CharField(max_length=20, choices=TECHNICIAN_TYPE_CHOICES, blank=True, null=True)  # Mechanicien ou Electricien

    def __str__(self):
        return f"{self.get_service_type_display()} request by {self.user.username}"

# Create your models here.
