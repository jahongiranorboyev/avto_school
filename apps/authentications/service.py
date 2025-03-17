from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import CustomUser


def get_user_from_refresh_token(refresh_token):
    try:
        token = RefreshToken(refresh_token)
        user_id = token['user_id']
        user = CustomUser.objects.get(id=user_id)
        return user
    except Exception:
        raise AuthenticationFailed({'error': 'Invalid refresh token'})
