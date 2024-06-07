from django import forms
from .models import AssistanceRequest, AssistanceMedia
from django.contrib.auth.models import User
class AssistanceRequestForm(forms.ModelForm):
    class Meta:
        model = AssistanceRequest
        fields = ['description', 'payment_method', 'assistance_type']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control input input-bordered w-full', 'rows': 3}),
            'payment_method': forms.Select(attrs={'class': 'form-control select select-bordered w-full'}),
            'assistance_type': forms.Select(attrs={'class': 'form-control select select-bordered w-full'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class AssistanceMediaForm(forms.ModelForm):
    class Meta:
        model = AssistanceMedia
        fields = ['media']
        widgets = {
            'media': forms.ClearableFileInput(attrs={'class': 'form-control', 'allow_multiple_selected': True}),
        }


