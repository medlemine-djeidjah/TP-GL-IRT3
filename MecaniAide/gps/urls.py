from django.urls import path
from . import views
from .views import update_location

urlpatterns = [
    path('', views.home, name='home'),
    path('update_location/', update_location, name='update_location'),
]
