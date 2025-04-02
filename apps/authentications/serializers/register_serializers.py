from django.core.cache import cache
from rest_framework import serializers

from apps.users.models import CustomUser
from apps.authentications.email import email_service



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        full_name = attrs['full_name']
        email_service.send_massage(email)
        cache.set(f'reg_{email}', {
            "email": email,
            "password": password,
            "full_name": full_name
        }, timeout=2 * 60)
        return attrs

