from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.create_service_request, name='service'),
]
