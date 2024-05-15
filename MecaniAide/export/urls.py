from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', include('export.urls')),
    # Autres URLs de votre application
]
