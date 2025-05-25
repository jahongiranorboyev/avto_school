import json
import base64
import logging

from django.utils.translation import gettext_lazy as _

from apps.utils.custom_exception import CustomAPIException

logger = logging.getLogger(__name__)


class Google:

    @staticmethod
    def validate(auth_token):
        try:
            logger.info(f"Validating token: {auth_token}")
            token_parts = auth_token.split('.')

            if len(token_parts) != 3:
                raise CustomAPIException(message=_("Invalid token format"))

            header_sp, payload_sp, signature_sp = token_parts
            payload_sp += "=" * (4 - len(payload_sp) % 4)
            decoded_payload = base64.urlsafe_b64decode(payload_sp)
            user_data = json.loads(decoded_payload)

            return user_data

        except Exception:
            raise CustomAPIException(message=_('Failed to decode token'))


