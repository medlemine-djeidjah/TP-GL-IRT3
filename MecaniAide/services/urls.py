# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.create_service_request, name='service'),
    path('service/<int:request_id>/update_status/', views.update_service_status, name='update_service_status'),
    path('service/<int:request_id>/add_response/', views.add_service_response, name='add_service_response'),
]
