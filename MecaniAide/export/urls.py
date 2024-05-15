from django.urls import path
from . import views

urlpatterns = [
    path('export-csv/', views.export_csv, name='export_csv'),
]
