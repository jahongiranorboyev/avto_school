from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from apps.payments.models import Order
from apps.general.models import General
from apps.users.models import CustomUser
from apps.utils.custom_exception import CustomAPIException


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'tariff', 'coupon_code']

    def validate_user_code(self, attrs):
        coupon_code = attrs['coupon_code']
        user = self.context['request'].user

        if not CustomUser.objects.filter(user_code=coupon_code).exists():
            raise CustomAPIException(message=_('Like this user code does not exist'))

        if user.user_code == coupon_code:
            raise CustomAPIException(message=_('You can not use yours user code'))

        if Order.objects.filter(user=user, coupon_code=coupon_code).exists():
            raise CustomAPIException(message=_('You already used this user code'))

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        tariff = validated_data.get('tariff')
        coupon_code = validated_data['coupon_code']

        if coupon_code is not None:
            return Order.objects.create(
                user_id=user.id,
                tariff_id=tariff.id,
                coupon_code=coupon_code,
            )
        else:

            return Order.objects.create(
                user_id=user.id,
                tariff_id=tariff.id,
            )
