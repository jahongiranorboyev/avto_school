from rest_framework import serializers

from apps.users.models import CustomUser
from apps.utils.custom_exception import CustomAPIException

from django.utils.translation import gettext_lazy as _

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)
    re_password = serializers.CharField(write_only=True, required=True, min_length=6 )
    email = serializers.EmailField(write_only=True)

    def validate(self, attrs):
        password = attrs['password']
        re_password = attrs['re_password']
        email = attrs['email']
        user: CustomUser | None = CustomUser.objects.filter(email=email).first()

        if password != re_password:
            raise CustomAPIException(message=_('There are passwords must be same'))

        if user is None or not user:
            raise CustomAPIException(message=_('user does not exist'))
        attrs.pop('re_password')
        user.set_password(password)
        user.save()
        return attrs

    def update(self, instance, validated_data):
        return instance