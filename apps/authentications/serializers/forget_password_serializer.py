from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from apps.users.models import CustomUser
from apps.utils.custom_exception import CustomAPIException


class ForgetPasswordSerializer(serializers.Serializer):
    """
        Serializer for initiating the password reset process.

        Fields:
            - email (str): The email address associated with the user account.

        Validation Logic:
            - Verifies if the email provided exists in the system (checks if the user is registered).
            - If the user is not found, raises a validation error indicating the user doesn't exist.
    """
    email = serializers.EmailField(required=True, write_only=True)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        """
          Validates the provided email for password reset.

          - Retrieves the user by email.
          - If the user is not found, raises a validation error.

          Returns:
              dict: The validated data (email in this case).

          Raises:
              ValidationError: If the user does not exist in the system.
        """
        email = attrs['email']
        user: CustomUser | None = CustomUser.objects.filter(email=email).first()

        if not user or user is None:
            raise CustomAPIException(message=_('The user we can not find try again please or remind clearly'))

        return attrs
