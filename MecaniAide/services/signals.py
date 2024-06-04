# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ServiceRequest, ServiceResponse

@receiver(post_save, sender=ServiceRequest)
def send_status_update_notification(sender, instance, **kwargs):
    if instance.status:
        send_mail(
            'Service Request Status Updated',
            f'The status of your service request "{instance.service_type}" has been updated to "{instance.get_status_display()}".',
            settings.DEFAULT_FROM_EMAIL,
            [instance.user.email],
        )

@receiver(post_save, sender=ServiceResponse)
def send_response_notification(sender, instance, **kwargs):
    send_mail(
        'New Response to Your Service Request',
        f'A new response has been added to your service request "{instance.service_request.service_type}".',
        settings.DEFAULT_FROM_EMAIL,
        [instance.service_request.user.email],
    )
