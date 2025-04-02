from rest_framework import serializers

from apps.general.models.tariff import Tariff


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'
        read_only_fields = ('id','created_at','updated_at','created_by','updated_by')