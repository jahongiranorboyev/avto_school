from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.users.models import CustomUser
from apps.utils.custom_exception import CustomAPIException


class RegisterVerifyCodeSerializer(serializers.Serializer):
    """
          Serializer for verifying the code sent to the user's email during registration.

          Accepts the user's email and verification code.
          Checks if the provided code matches the one stored in the cache.
          If valid, clears the code from the cache and proceeds with registration.
    """
    email = serializers.EmailField(write_only=True)
    code = serializers.CharField(write_only=True)
    CACHE_USER_CODE = 'user_code_{email}'
    CACHE_USER_DATA = 'reg_{email}'

    def validate(self, attrs):
        """
           Validates the code submitted by the user.

           - Retrieves the stored verification code from cache using the email.
           - Retrieves the temporary user data also stored during registration.
           - If the code or user data doesn't match, raises a validation error.
           - On success, deletes the code from cache (user data will be used in the next step).

           Returns:
               dict: The validated data containing the email.
        """
        code = attrs['code']
        email = attrs['email']
        re_code = self.CACHE_USER_CODE.format(email=email)
        user_data = self.CACHE_USER_DATA.format(email=email)

        saved_code = cache.get(re_code)
        user_data = cache.get(user_data)

        if saved_code is None or str(code) != str(saved_code):
            raise CustomAPIException(message=_('The code is wrong or time is out'))

        if user_data is None or user_data['email'] != email:
            raise CustomAPIException(message=_('we have some problem try again later'))


        attrs['email'] = email
        return attrs

    def create(self, validated_data):
        """
            Creates a new user using the data temporarily stored in the cache.

            - Retrieves cached user data (email, hashed password, full name).
            - Uses `create_user` method to create and save the user.
            - Deletes the cached user data after successful creation.

            Args:
                validated_data (dict): Validated data containing the user's email.

            Returns:
                CustomUser: The newly created user instance.
        """
        email = validated_data['email']

        # ======= Get user data from cache based on email ============
        user_data = cache.get(self.CACHE_USER_DATA.format(email=email))

        # ============ Create user using custom create_user method ================
        if email == user_data['email']:
            user = CustomUser.objects.create(
                email=email,
                password=user_data['password'],
                full_name=user_data['full_name'],
            )
            cache.delete(self.CACHE_USER_DATA.format(email=email))

            return user

        # ======= Clean up: Remove cached data after user is created ============
        return {'filed'}


class ForgetPasswordVerifyCodeSerializer(serializers.Serializer):
    """
       Serializer for verifying a code sent to the user's email for password reset.

       Fields:
           - code (int): The verification code sent to the user's email.
           - email (str): The email address to which the code was sent.

       Validation logic:
           - Checks if a user with the given email exists.
           - Retrieves the saved verification code from cache and compares it with the provided code.
           - Raises a validation error if the user does not exist or the code is incorrect/expired.
    """
    code = serializers.IntegerField(required=True, write_only=True)
    email = serializers.EmailField(write_only=True)
    CACHE_USER_CODE = 'user_code_{email}'

    def validate(self, attrs):
        code = attrs['code']
        email = attrs['email']

        # ===== Get saved verification code from cache =====
        saved_code = cache.get(self.CACHE_USER_CODE.format(email=email))

        # ===== Check if a user with the given email exists =====
        user: CustomUser | None = CustomUser.objects.filter(email=email).first()

        if user is None or user.email != email:
            raise CustomAPIException(message=_('Like this user not here'))

        # ===== Validate the code =====
        if not saved_code or str(code) != str(saved_code):
            raise CustomAPIException(message=_('The code is wrong or time is out'))

        # ===== If everything is fine, return validated data =====
        return attrs
