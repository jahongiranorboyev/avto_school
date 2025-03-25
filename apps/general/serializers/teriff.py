from rest_framework import serializers

from apps.general.models import tariff

class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = tariff.Tariff
        fields = '__all__'
        read_only_fields = ('created_at','updated_at','created_by','updated_by')

