from decimal import Decimal

from apps.utils.models import BaseModel

from django.db import models
from django.utils.translation import gettext_lazy as _


class Tariff(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )
    days = models.IntegerField(
        default=0,
        verbose_name=_('Days'),
    )
    price = models.DecimalField(
        default=Decimal('0'),
        verbose_name=_('Price'),
        decimal_places=2,
        max_digits=10,
    )
    discount = models.ForeignKey(
        to='general.Discount',
        on_delete=models.PROTECT,
        verbose_name=_('Discount'),
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.title}"

    def discount_coupon(
            self, new_price=None, user=None,
            general_obj=None, user_order=None, mode=None
    ) -> Decimal:
        """
            Calculates the adjusted price of the tariff based on the given mode.

            Parameters:
                new_price (Decimal, optional): Unused in logic, can be extended for future.
                user (User, optional): The current user, used to access balance.
                general_obj (General, optional): General site-wide discount configuration.
                user_order (Order, optional): The current user's unpaid order, used to apply coupon.
                mode (str, optional): Determines logic flow ('coupon', 'balance', or None).

            Returns:
                Decimal: The final discounted price based on the given context.
        """
        temp_price = self.price
        discount_obj = self.discount

        if mode is None:
            temp_price = 0

        if mode == 'coupon':
            if user_order is not None:
                if (
                        user_order is not None and
                        user_order.created_at is not None and
                        user_order.is_paid == False and
                        user_order.coupon_code is not None
                ):
                    if general_obj is None:
                        temp_price = 0
                        return temp_price
                    elif general_obj.user_code_discount_is_percent == False:
                        discount = temp_price - (temp_price * general_obj.user_code_discount / 100)
                        print(discount, 'DDDDDDDDDDDDDDDDDDDDDDDDDdd')
                        print(temp_price-discount, '______________________-----')
                        return temp_price - discount
                    print('FFFFFFFFFFFFFFFFFFfffff')
                    return temp_price - general_obj.user_code_discount
        elif mode == 'balance':
            if user is not None:
                if discount_obj is not None and discount_obj.is_percent == True:
                    temp_price -= temp_price * discount_obj.amount / 100
                elif discount_obj is not None and discount_obj.is_percent == False:
                    temp_price -= discount_obj.amount
            if user:
                if user.balance >= temp_price:
                    return Decimal('0')
                return temp_price - user.balance
        return temp_price


