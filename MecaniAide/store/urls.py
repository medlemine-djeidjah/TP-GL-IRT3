from django.urls import path
from .views import car_parts_store, car_parts_store_api, shop_cart, checkout

urlpatterns = [
    path('store', car_parts_store, name='car_parts_store'),
    path('cart', shop_cart, name='shop_cart'),
    path('api/car-parts-store/', car_parts_store_api, name='car_parts'),
     path('checkout/', checkout, name='checkout'),
]
