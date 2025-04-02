from rest_framework import serializers

from apps.users.models import CustomUser

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)
    re_password = serializers.CharField(write_only=True, required=True, min_length=6 )

    def validate(self, attrs):
        password = attrs['password']
        re_password = attrs['re_password']
        token = self.context.get('kwargs').get('token')
        encoded_pk = self.context.get('kwargs').get('encoded_pk')

        if password != re_password:
            raise serializers.ValidationError({'Value error': 'There are passwords must be same'})

        if token is None or encoded_pk is None:
            raise serializers.ValidationError({'error': 'Missing data'})


        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = CustomUser.objects.get(pk=pk)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError('The reset token invalid')

        attrs.pop('re_password')
        user.set_password(password)
        user.save()
        return attrs
