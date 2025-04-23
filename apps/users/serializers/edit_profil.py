from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from apps.utils.custom_exception import CustomAPIException


class EditProfileSerializer(serializers.Serializer):
    re_password = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    icon = serializers.ImageField(required=False, allow_null=True)
    first_name = serializers.CharField(max_length=30, required=False)

    def validate(self, attrs):
        request = self.context.get('request')
        password = attrs.get('password', '')
        re_password = attrs.get('re_password', '')

        user = request.user
        if not user or not user.is_authenticated:
            raise CustomAPIException(_('User did not register'))

        if password != re_password:
            raise CustomAPIException(_('Password and Re Password must be equal please check it'))

        return attrs

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        icon = validated_data.get('icon', None)

        if icon:
            instance.icon = icon
        if password:
            instance.set_password(password)

        for attr, value in validated_data.items():
            if attr != 'password':
                setattr(instance, attr, value)

        instance.save()
        return instance
