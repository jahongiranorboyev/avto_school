from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


class LogoutSerializer(serializers.Serializer):
    """
        Serializer for logging out a user by blacklisting the refresh token.

        - Accepts a refresh token from the user to invalidate it.
        - Validates the token and then blacklists it using `RefreshToken`.
        - If the token is invalid or an error occurs, a validation error is raised.
    """
    refresh_token = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """
           Validates the provided refresh token.

           - Extracts the refresh token from the request data.
           - Returns the validated token data.

           Returns:
               dict: Contains the refresh token.
        """
        self.token = attrs['refresh_token']
        return attrs

    def save(self, **kwargs):
        """
           Handles the process of blacklisting the refresh token.

           - Attempts to blacklist the token using `RefreshToken`.
           - If the token is valid and successfully blacklisted, the logout process completes.
           - If the token is invalid or an error occurs, a `TokenError` is raised.

           Raises:
               TokenError: If the token is invalid or cannot be blacklisted.
        """
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('token failed')


