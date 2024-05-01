from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class PhoneBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(phone_number=phone_number)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None
