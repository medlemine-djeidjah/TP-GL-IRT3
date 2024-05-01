from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

class PhoneLoginForm(AuthenticationForm):
    phone_number = forms.CharField(label='Phone Number', max_length=15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)  # Remove the 'username' field
        self.fields['phone_number'].widget.attrs['autofocus'] = False

    def clean_username(self):
        return self.cleaned_data['phone_number']

    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'password']


class PhoneRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=150)  # Add 'username' field

    class Meta:
        model = get_user_model()
        fields = ['username', 'phone_number', 'password']  # Add 'username' field
