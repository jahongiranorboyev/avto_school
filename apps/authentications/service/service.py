from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import CustomUser
from apps.utils.custom_exception import CustomAPIException

from django.utils.translation import gettext_lazy as _

def get_user_from_refresh_token(refresh_token):
    try:
        token = RefreshToken(refresh_token)
        user_id = token['user_id']
        user = CustomUser.objects.get(id=user_id)
        return user
    except Exception:
        raise CustomAPIException(message=_('Invalid refresh token'))
