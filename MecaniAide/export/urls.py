<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('export-csv/', views.export_csv, name='export_csv'),
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', include('export.urls')),
    # Autres URLs de votre application
>>>>>>> 5dc325a283b77d22535eae61e57aa24aaa759670
]
