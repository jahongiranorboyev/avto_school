from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel

class Order(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    tariff = models.ForeignKey('payments.Tariff', on_delete=models.PROTECT)
    days = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )
    expire_date = models.DateField(
        null=True,
        blank=True
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=True,
        null=True
    )
    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    is_paid = models.BooleanField(default=False)
    coupon_code = models.CharField(
        max_length=8,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.id}" if self.user else "No User"

    class Meta:
        unique_together = ('user', 'coupon_code')

