from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.html import mark_safe
from import_export.admin import ImportExportModelAdmin
from PIL import Image
from io import BytesIO
import base64
class AssistanceRequest(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Bankily', 'Bankily'),
        ('Sedad', 'Sedad'),
        ('cash', 'Cash'),
        ('BimBank', 'BimBank'),
        ('Masrivi', 'Masrivi'),
    ]

    ASSISTANCE_TYPE_CHOICES = [
        ('towing', 'Towing'),
        ('flat_battery', 'Flat Battery'),
        ('flat_tire', 'Flat Tire'),
        ('lockout', 'Lockout'),
        ('fuel_delivery', 'Fuel Delivery'),
        ('Diagnostic', 'Diagnostic'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    assistance_type = models.CharField(max_length=20, choices=ASSISTANCE_TYPE_CHOICES)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    forwarded_to = models.ForeignKey(User, related_name='forwarded_requests', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Request by {self.user.username} for {self.get_assistance_type_display()} at {self.created_at}'

    def get_first_media_url(self):
        first_media = self.media.first()
        if first_media:
            return first_media.media.url
        return None
    
class AssistanceMedia(models.Model):
    assistance_request = models.ForeignKey(AssistanceRequest, related_name='media', on_delete=models.CASCADE)
    media = models.FileField(upload_to='assistance_media/')

    def __str__(self):
        return f'Media for request {self.assistance_request.id}'



class AssistanceMediaInline(admin.TabularInline):
    model = AssistanceMedia
    extra = 0

    def media_file_link(self, obj):
        return mark_safe(f'<a href="{obj.media.url}">{obj.media.name}</a>')
    media_file_link.short_description = 'Media File'

    def preview_image(self, obj):
        if obj.media.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                # Open image using Pillow
                image = Image.open(obj.media)
                # Create thumbnail
                image.thumbnail((100, 100))
                # Convert image to BytesIO object
                image_data = BytesIO()
                image.save(image_data, format=image.format)
                # Encode image data as base64
                encoded_image_data = base64.b64encode(image_data.getvalue()).decode()
                # Generate HTML to display thumbnail
                return mark_safe(f'<img src="data:image/{image.format};base64,{encoded_image_data}" height="100"/>')
            except Exception as e:
                return mark_safe(f'<span style="color:red;">Error: {e}</span>')
        return None
    preview_image.short_description = 'Preview'

    readonly_fields = [ 'preview_image']

class AssistanceRequestAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user','description' ,'assistance_type', 'created_at')
    inlines = [AssistanceMediaInline]

admin.site.register(AssistanceRequest, AssistanceRequestAdmin)