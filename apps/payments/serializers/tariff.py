from rest_framework import serializers

from apps.payments.models import Tariff


class TariffSerializer(serializers.ModelSerializer):
    """
        Serializer for the Tariff model that dynamically computes pricing information
        such as discounted price, user balance usage, and applied user/coupon discounts
        depending on the mode and context.
    """
    new_price = serializers.SerializerMethodField(required=False, read_only=True)
    balance = serializers.SerializerMethodField(required=False, read_only=True)
    user_code_discount = serializers.SerializerMethodField(required=False, read_only=True)
    discount_price = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = Tariff
        fields = '__all__'
        read_only_fields = (
            'id', 'created_at', 'updated_at', 'created_by', 'updated_by'
        )
    def _get_user(self):
        """Returns the user from the request context."""
        return self.context['request'].user

    def _get_mode(self):
        """Returns the serialization mode from context ('default', 'coupon', 'balance', etc.)."""
        return self.context.get('mode')

    def _get_general_obj(self):
        """Returns the general_obj from context, which may contain user discount data."""
        return self.context.get('general_obj')

    def _get_user_order(self):
        """Returns the user_order from context, used in discount calculations."""
        return self.context.get('user_order')

    def get_new_price(self, obj):
        """
            Calculates the final price after applying all discounts (coupon, balance, etc.)
            using the Tariff model's `discount_coupon()` method.
        """
        return obj.discount_coupon(
            new_price=None,
            user=self._get_user(),
            general_obj=self._get_general_obj(),
            user_order=self._get_user_order(),
            mode=self._get_mode()
        )

    def get_balance(self, obj):
        """
            Calculates the amount that will be subtracted from the user's balance.
            Returns the negative value to represent deduction.
        """
        user = self._get_user()
        return -min(user.balance, obj.price)

    def get_user_code_discount(self, obj):
        """
            Calculates the discount from a user-provided referral or coupon code.
            Returns the negative discount amount if applicable.
        """
        general_obj = self._get_general_obj()
        if general_obj is None:
            return None
        discount = general_obj.user_code_discount
        if general_obj.user_code_discount_is_percent == True:
            return -(obj.price * discount / 100)
        return -discount

    def get_discount_price(self, obj):
        """
            Calculates the built-in discount defined on the Tariff object.
            Returns the negative discount amount if available.
        """
        if obj.discount is None:
            return None

        discount = obj.discount.amount
        if obj.discount.is_percent:
            return -(obj.price * discount / 100)
        return -discount


    def to_representation(self, instance):
        """
            Customizes the serialized output based on the `mode` and context data.
            Removes pricing-related fields conditionally to avoid unnecessary exposure.
        """
        data = super().to_representation(instance)
        user = self._get_user()
        mode = self._get_mode()
        fields_to_remove = set()
        if mode == 'default':
            """
                In 'default' mode, remove all dynamic discount/balance fields.
                Only static tariff fields are returned.
            """
            fields_to_remove.update(['new_price', 'balance', 'user_code_discount', 'discount_price'])

        elif mode == 'coupon':
            if self._get_user_order() is None:
                fields_to_remove.update(['discount_price', 'balance', 'user_code_discount', 'new_price'])
            """
                In 'coupon' mode, show only the result of coupon discount.
                Do not show balance-related or built-in discount data.
            # """
            if self._get_user_order() is not None:
                fields_to_remove.update(['discount_price', 'balance'])


        elif mode == 'balance':
            """
                In 'balance' mode, hide user-code discounts. Show or hide tariff discount based on its existence.
            """
            if instance.discount is None and user.balance <=0:
                fields_to_remove.update(['discount_price', 'user_code_discount', 'balance', 'new_price'])

            elif instance.discount is not None:
                fields_to_remove.update(['user_code_discount', 'balance', ])

            elif user.balance > 0:
                fields_to_remove.update(['user_code_discount', 'discount_price'])

        for field in fields_to_remove:
            data.pop(field, None)

        return data
