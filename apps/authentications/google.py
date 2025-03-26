from google.auth.transport import requests
from google.oauth2 import id_token
from django.conf import settings
from rest_framework import serializers


class Google:

    @staticmethod
    def validate(auth_token):

        try:
            id_info = id_token.verify_oauth2_token(
                auth_token, requests.Request(), settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY)
            if 'accounts.google.com' in id_info['iss']:
                return id_info
        except ValueError:
            raise serializers.ValidationError({"error": "The token invalid or has expired"})