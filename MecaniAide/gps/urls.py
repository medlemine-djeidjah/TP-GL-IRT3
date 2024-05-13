from django.urls import path
from . import views
from .views import tracking

urlpatterns = [
    path('', views.home, name='home'),
    path('tracking/', tracking, name='tracking'),
]
