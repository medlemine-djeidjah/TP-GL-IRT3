# forms.py
from django import forms
from .models import ServiceRequest, ServiceResponse

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description', 'payment_method', 'image', 'video', 'litres', 'fuel_type', 'car_brand', 'technician_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'service_type': forms.Select(),
            'payment_method': forms.Select(),
        }


    def clean(self):
        cleaned_data = super().clean()
        service_type = cleaned_data.get('service_type')

        if service_type == 'fuel_delivery':
            if cleaned_data.get('litres') is None:
                raise forms.ValidationError("Le nombre de litres est requis pour le service de livraison de carburant.")
            if not cleaned_data.get('fuel_type'):
                raise forms.ValidationError("Le type de carburant est requis.")

        if service_type == 'lost_key' and not cleaned_data.get('car_brand'):
            raise forms.ValidationError("La marque de la voiture est requise pour le service de clé perdue.")

        if service_type == 'diagnostic' and not cleaned_data.get('technician_type'):
            raise forms.ValidationError("Le type de technicien est requis pour le diagnostic.")

        return cleaned_data

class ServiceStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']

class ServiceResponseForm(forms.ModelForm):
    class Meta:
        model = ServiceResponse
        fields = ['response']
        widgets = {
            'response': forms.Textarea(attrs={'rows': 3}),
        }
