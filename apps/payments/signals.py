from celery.utils.time import remaining
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save

from datetime import timedelta
from apps.payments.models import Order
from apps.general.models import General
from apps.users.models import CustomUser


@receiver((pre_save,), sender=Order)
def post_save_order_expire_date(sender, instance, *args, **kwargs):

    user = instance.user

    if instance.is_paid:

        if instance.tariff:
            instance.days = instance.tariff.days
            instance.expire_date = timezone.now() + timedelta(days=instance.tariff.days)

            if user.order_expire_date >= timezone.now():
                user.order_expire_date += timedelta(days=instance.tariff.days)
            else:
                user.order_expire_date = timezone.now() + timedelta(days=instance.tariff.days)


            user.save(update_fields=['order_expire_date'])


@receiver((pre_save,), sender=Order)
def subtract_price_of_tariff_by_balance_and_discount(sender,instance, *args, **kwargs):

    user = instance.user
    tariff = instance.tariff
    tariff_discount = instance.tariff.discount
    general = General.objects.all().first()
    user_friend = CustomUser.objects.filter(user_code=instance.coupon_code).first()
    remaining_price = tariff.price if tariff else 0
    discount = 0

    if instance.is_paid:
        if general is not None and instance.coupon_code is not None and general.user_code_discount_is_percent is True:

            discount = tariff.price * general.user_code_discount / 100
            remaining_price = tariff.price - discount
            if user_friend is not None:
                user_friend.balance += discount
            user.balance += discount

        elif general is not None and instance.coupon_code is not None and general.user_code_discount_is_percent is False:
            discount = tariff.price - general.user_code_discount
            remaining_price = general.user_code_discount
            if user_friend is not None:
                user_friend.balance += discount
            user.balance += discount

        elif tariff and user:
            if tariff_discount is not None and tariff_discount.is_percent is True and instance.coupon_code is None:
                discount = tariff.price * tariff_discount.amount / 100
                remaining_price = tariff.price - discount

            elif tariff_discount is not None and tariff_discount.is_percent is False and instance.coupon_code is None:
                discount = tariff.price - tariff_discount.amount
                remaining_price = tariff_discount.amount

            elif user.balance >= tariff.price and tariff_discount is None and instance.coupon_code is None:
                discount =  tariff.price
                remaining_price = 0
                user.balance -= discount

            elif user.balance <= tariff.price and tariff_discount is None and instance.coupon_code is None:
                discount = user.balance
                remaining_price = tariff.price - discount
                user.balance = 0
        instance.price = remaining_price
        instance.discount_price = discount
        if user_friend is not None:
            user_friend.save(update_fields=['balance'])
        user.save(update_fields=['balance'])
    else:
        if general is not None and instance.coupon_code is not None and general.user_code_discount_is_percent is True:
            discount = tariff.price * general.user_code_discount / 100
            remaining_price = tariff.price - discount

        elif general is not None and instance.coupon_code is not None and general.user_code_discount_is_percent is False:
            discount = tariff.price - general.user_code_discount
            remaining_price = general.user_code_discount

        instance.price = remaining_price
        instance.discount_price = discount
