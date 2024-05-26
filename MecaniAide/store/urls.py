from django.urls import path
from .views import car_parts_store, car_parts_store_api

urlpatterns = [
    path('store', car_parts_store, name='car_parts_store'),
    path('api/car-parts-store/', car_parts_store_api, name='car_parts'),
]
