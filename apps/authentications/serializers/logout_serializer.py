from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


class LogoutSerializer(serializers.Serializer):

    def validate(self, attrs):
        """
         this is
        """
        request = self.context.get('request')
        if request is None:
            raise serializers.ValidationError({'error': 'Request object is missing from context.'})

        if not hasattr(request, 'session'):
            raise serializers.ValidationError({'error': 'Session object is not available in request.'})

        refresh_token = request.session.get('refresh_token')
        if not refresh_token:
            raise serializers.ValidationError({'token': 'it is enable in session'})

        self.token = refresh_token
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('token failed')

        request = self.context.get('request')

        request.session.pop('refresh_token', None)

