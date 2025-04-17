import time
import string
import random

from rest_framework import serializers

from apps.authentications import google
from apps.users.models import CustomUser
from apps.general.views.custom_xception import CustomAPIException
from apps.authentications.social_register.register import register_social_user

from django.conf import settings
from django.utils.translation import gettext_lazy as _

def generate_reset_code():
    """ random code generate for send to user when user forget and"""
    exists_code = set(CustomUser.objects.values_list('user_code', flat=True))
    while True:
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choices(characters, k=8))
        if code not in exists_code:
            return code



class GoogleSocialAuthSerializer(serializers.Serializer):
    id_token = serializers.CharField()

    def validate_auth_token(self, id_token):
        """
        Google tokenini dekodlash va foydalanuvchini aniqlash
        """
        user_data = google.Google.validate(id_token)
        try:
            user_data['sub']
        except:
            raise CustomAPIException(
                message=_('The token is invalid or expired. Please login again')
            )
        if 'error' in user_data:
            raise CustomAPIException(message=_('this just error i do not what happen'))

        if user_data.get('iss') not in ["https://accounts.google.com", "accounts.google.com"]:
            raise CustomAPIException(message=_('Invalid token issuer'))

        if user_data['aud'] != settings.SOCIAL_AUTH_GOOGLE_OAUTH2_ID and user_data.get('azp') != settings.SOCIAL_AUTH_GOOGLE_OAUTH2_ID:
            raise CustomAPIException(message= _("oops who are you this id token wrong"))

        current_time = int(time.time())
        if user_data.get("exp") < current_time:
            raise ValueError({'error': 'Token has expired'})

        email = user_data['email']
        name = user_data['name']
        user_code = generate_reset_code()
        provider = 'google'
        data = {
            'provider':provider,
            'email':email,
            'full_name':name,
            'user_code':user_code}
        return data

    def create(self, validated_data):
        id_token = validated_data.get("id_token")
        data = self.validate_auth_token(id_token)
        user = register_social_user(**data)
        return user