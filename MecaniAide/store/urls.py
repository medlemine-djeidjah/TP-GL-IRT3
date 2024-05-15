from django.urls import path
from .views import car_parts_store

urlpatterns = [
    path('store', car_parts_store, name='car_parts_store'),
]
