from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from  rest_framework import serializers

from apps.utils.custom_exception import CustomAPIException


class ReSendVerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    CACHE_USER_CODE = 'user_code_{email}'
    CACHE_USER_EMAIL = 'user_email_{code}'

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs['email']
        try:
            print(self.CACHE_USER_EMAIL, email)
            saved_code = cache.get(self.CACHE_USER_CODE.format(email=email))
        except Exception:
            raise CustomAPIException(message=_('You should try again later'))

        attrs['saved_code'] = saved_code
        return attrs

