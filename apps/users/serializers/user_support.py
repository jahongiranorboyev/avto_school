from rest_framework import serializers

from apps.users.models import Support


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'
