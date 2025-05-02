import random
import string

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from apps.payments.models import Order
from datetime import timedelta
from django.utils import timezone

from apps.users.models import CustomUser


@receiver(post_save, sender=Order)
def update_user_order_expire_date(sender, instance, created, **kwargs):
    user = instance.user
    total_days = sum(order.days for order in user.order_set.all())

    user.order_expire_date = timezone.now().date() + timedelta(days=total_days)
    user.save(update_fields=['order_expire_date'])


@receiver(pre_save, sender=CustomUser)
def change_of_user_some_fields_after_create(sender, instance, **kwargs):
        instance.order_expire_date = timezone.now() - timedelta(days=1)
        instance.coins = 10
        exists_code = set(CustomUser.objects.values_list('user_code', flat=True))
        while True:
            characters = string.ascii_letters + string.digits
            code = ''.join(random.choices(characters, k=8))
            if code not in exists_code:
                instance.user_code = code
                break
