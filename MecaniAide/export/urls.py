from django.urls import path
from .views import upload_csv, export_csv

urlpatterns = [
    path('upload-csv/', upload_csv, name='upload_csv'),
    path('export-csv/', export_csv, name='export_csv'),
]

