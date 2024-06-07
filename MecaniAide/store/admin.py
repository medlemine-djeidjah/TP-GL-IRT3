from django.contrib import admin
from .models import CarPart, OrderItem

# Register your models here.
admin.site.register(CarPart)
admin.site.register(OrderItem)