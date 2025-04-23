from rest_framework import serializers

from apps.general.models import Tariff


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'
        read_only_fields = ('id','created_at','updated_at','created_by','updated_by')

        def to_representation(self, instance):
            representation = super().to_representation(instance)

            representation['price'] = f"${instance.price:.2f}"
            representation['created_at'] = instance.created_at.strftime("%Y-%m-%d")  # custom date format

            return representation