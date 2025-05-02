from rest_framework import serializers

from apps.users.models import CustomUser


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_code']