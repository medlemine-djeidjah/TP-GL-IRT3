from django.urls import path
from . import views

urlpatterns = [
    path('incident_form', views.create_service_request, name='incident_form'),
]
