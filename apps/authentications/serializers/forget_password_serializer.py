from rest_framework import serializers
from apps.users.models import CustomUser


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs['email']
        user = CustomUser.objects.filter(email=email)
        if not user:
            raise serializers.ValidationError({'error': 'The user we can not find try again please or remind clearly'})
        return attrs
