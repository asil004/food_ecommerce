from django.contrib.auth.hashers import check_password
from django.db.models import Q
from .models import User


class CustomUserAuth:
    def authenticate(self, request, email_or_phone=None, password=None):
        try:
            user = User.objects.get(
                Q(email=email_or_phone) | Q(phone_number=email_or_phone)
            )
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
