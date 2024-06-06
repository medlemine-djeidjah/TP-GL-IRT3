# models.py
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

# Choix pour le statut
STATUS_CHOICES = [
    ('open', 'Open'),
    ('in_progress', 'In Progress'),
    ('resolved', 'Resolved'),
    ('closed', 'Closed'),
]

class ServiceRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField(blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    video = models.FileField(upload_to='service_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    litres = models.FloatField(blank=True, null=True)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES, blank=True, null=True)
    car_brand = models.CharField(max_length=50, blank=True, null=True)
    technician_type = models.CharField(max_length=20, choices=TECHNICIAN_TYPE_CHOICES, blank=True, null=True)
    technician = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_requests', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.get_service_type_display()} request by {self.user.username}"

class ServiceResponse(models.Model):
    service_request = models.ForeignKey(ServiceRequest, related_name='responses', on_delete=models.CASCADE)
    responder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Response by {self.responder.username} on {self.service_request}'
