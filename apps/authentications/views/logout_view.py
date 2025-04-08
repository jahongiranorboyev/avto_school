from tokenize import TokenError

from apps.users.models import CustomUser

from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed


def get_user_from_refresh_token(refresh_token):
    try:
        token = RefreshToken(refresh_token)
        user_id = token['user_id']
        user = CustomUser.objects.get(id=user_id)
        return user
    except Exception:
        raise AuthenticationFailed({'error': 'Invalid refresh token'})


class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token is None:
            raise ValueError({'error': 'No refresh token provider'})
        token = RefreshToken(refresh_token)
        user_from_token = get_user_from_refresh_token(refresh_token)
        if request.user.id == user_from_token.id:
            raise ValueError({'error': 'This user not here'})
        try:
            token.blacklist()
        except TokenError:
            raise ValueError({'error': 'Token invalid or already used'})
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)



