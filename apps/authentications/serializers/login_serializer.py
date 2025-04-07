from apps.users.models import CustomUser
from django.contrib import auth
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    refresh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        filter_user_by_email = CustomUser.objects.filter(email=email).first()

        user = auth.authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError({"error": "Email yoki parol noto‘g‘ri"})
        if not user.is_active:
            raise AuthenticationFailed({'error': 'Account disabled, contact admin '})

        if not user.check_password(password):
            raise serializers.ValidationError({"error": "Email yoki parol noto‘g‘ri"})

        if filter_user_by_email.auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using' + filter_user_by_email[0].auth_provider
            )


        return {
            "tokens" : filter_user_by_email.tokens()
        }
