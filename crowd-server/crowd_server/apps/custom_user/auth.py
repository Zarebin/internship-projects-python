from django.contrib.auth.backends import BaseBackend
from .models import User


class EmailBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username'].lower()  
        password = kwargs['password']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.is_active and user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


