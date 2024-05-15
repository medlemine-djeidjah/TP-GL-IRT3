from django.urls import path
from . import views

urlpatterns = [
    path('view-profile/', views.view_profile, name='view_profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
]
