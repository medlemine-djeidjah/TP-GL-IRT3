from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service-providers-map/', views.service_providers_map, name='service_providers_map'),
]
