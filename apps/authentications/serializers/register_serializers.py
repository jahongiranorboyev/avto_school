from rest_framework import serializers

from django.core.cache import cache
from django.contrib.auth.hashers import make_password

from apps.users.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    """
        Serializer for registering a new user.

        Accepts email, password, and full name.
        Sends a verification message to the user's email and temporarily stores user data in cache.
    """
    CACHE_KEY_RE = 'reg_{email}'
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        """
            Validates the input data for user registration.

            - Sends a confirmation or verification message to the provided email.
            - Hashes the password and stores the user data in the cache for 1 hour.

            Returns:
                dict: The validated and processed data.
        """
        email = attrs['email']
        password = attrs['password']
        full_name = attrs['full_name']
        key = self.CACHE_KEY_RE.format(email=email)
        cache.set(key, {
            "email": email,
            "password": make_password(password),
            "full_name": full_name
        }, timeout=60 * 60)
        print(cache.get(key))

        return attrs

