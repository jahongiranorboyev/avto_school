from rest_framework import serializers

from apps.payments.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = instance.user
        tariff = instance.tariff
        data['user'] = {
            'id': user.id,
            'full_name': user.full_name,
            'balance': user.balance,
        }
        data['tariff'] = {
            'id': tariff.id,
            'price': tariff.price,
            'discount': tariff.discount,
            'created_at': tariff.created_at,
        }
        return data