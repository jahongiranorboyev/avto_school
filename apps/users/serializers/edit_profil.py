from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.users.models import CustomUser
from apps.utils.custom_exception import CustomAPIException


class EditProfileSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = ['password', 're_password', 'full_name']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'full_name': {'required': False}
        }
