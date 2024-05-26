# apps.py
from django.apps import AppConfig

class ServiceConfig(AppConfig):
    name = 'services'

    def ready(self):
        import services.signals
