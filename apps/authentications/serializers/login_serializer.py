from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.users.models import CustomUser
from apps.utils.custom_exception import CustomAPIException


class LoginSerializer(serializers.Serializer):
    """
        Serializer for user login.

        Accepts user credentials (email and password) and returns JWT refresh and access tokens
        upon successful authentication.

        - The `email` and `password` are provided by the user to log in.
        - Upon successful authentication, the user will receive the `access_token` and `refresh_token`.
        - If authentication fails, an error message is raised.
    """
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    refresh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        """
            Validates the provided email and password.

            This method authenticates the user using Django's built-in authentication system.
            If the authentication is successful, it returns the user's JWT tokens.
            If the authentication fails, it raises a validation error with an appropriate message.

            Parameters:
            attrs (dict): The input data containing 'email' and 'password'.

            Returns:
            dict: Contains 'access_token' and 'refresh_token' if the authentication is successful.

            Raises:
            serializers.ValidationError: If the authentication fails.
        """
        email = attrs.get("email")
        password = attrs.get("password")

        user: CustomUser | None = CustomUser.objects.filter(email=email).first()
        if user is None:
            raise CustomAPIException(
                message=_("Email or password is incorrect. Please check and try again.")
            )
        if not user.check_password(password):
            raise CustomAPIException(message=_("Email or password is incorrect. Please check and try again."))

        return {
            'access_token': user.tokens()['access'],
            'refresh_token': user.tokens()['refresh']
        }



