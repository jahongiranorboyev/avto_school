from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.payments.models import Order


@receiver((post_save,), sender=Order)
def post_save_order_expire_date(sender,instance, created, *args, **kwargs):
    if created:
        instance.expire_date = timezone.now()
        instance.save(update_fields=['expire_date'])
