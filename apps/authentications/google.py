import logging
import base64
import json

from rest_framework import serializers
from tokenize import TokenError

logger = logging.getLogger(__name__)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '603070947700-uhru8mm50534bfm6s1q0ofnlu2lh4hm8.apps.googleusercontent.com'


class Google:

    @staticmethod
    def validate(auth_token):
        try:
            logger.info(f"Validating token: {auth_token}")
            token_parts = auth_token.split('.')

            if len(token_parts) != 3:
                raise serializers.ValidationError({"error": "Invalid token format"})

            header_sp, payload_sp, signature_sp = token_parts
            payload_sp += "=" * (4 - len(payload_sp) % 4)
            decoded_payload = base64.urlsafe_b64decode(payload_sp)
            user_data = json.loads(decoded_payload)

            return user_data

        except Exception as e:
            raise TokenError({'error': f'Failed to decode token: {str(e)}'})


