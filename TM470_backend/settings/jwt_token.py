from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework.exceptions import Throttled
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .throttling import LoginAnonThrottle, LoginUserThrottle

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': 'Incorrect Username or Password'
    }

    @classmethod
    def get_token(cls, user):
        update_last_login(None, user)
        return super().get_token(user=user)

    def validate(self, attrs):
        return super().validate(attrs)


class CustomTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [LoginAnonThrottle, LoginUserThrottle]
    serializer_class = CustomTokenObtainPairSerializer

    def throttled(self, request, wait):
        raise Throttled(detail={
            "detail": f"Account locked. Try again in {wait} seconds",
            "availableIn": f"{wait} seconds",
            "throttleType": "type"
        })
