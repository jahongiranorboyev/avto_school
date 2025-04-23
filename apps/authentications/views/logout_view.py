from rest_framework import status, generics

from apps.authentications.serializers import LogoutSerializer


class LogoutView(generics.CreateAPIView):
    """
       API view for logging out a user by blacklisting their refresh token.

       - Validates the provided refresh token.
       - Blacklists the refresh token to log the user out.
       - Returns a response indicating successful logout.
    """
    serializer_class = LogoutSerializer
    permission_classes = ()
    authentication_classes = ()