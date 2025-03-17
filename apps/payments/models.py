from django.db import models

from apps.utils.models import BaseModel
from config import settings


class Order(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    tariff = models.ForeignKey('general.Tariff', on_delete=models.PROTECT)
    days = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )
    expire_date = models.DateTimeField(
        null=True,
        blank=True
    )
    price = models.FloatField(
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

    def __str__(self):
        return self.user.username


class Transaction(BaseModel):
    class State(models.IntegerChoices):
        AWAITING_PAYMENT = 1
        COMPLETED = 2
        DOES_NOT_EXIST = -1
        CANCELLED = -2

    state = models.IntegerField(choices=State, default=State.AWAITING_PAYMENT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    performed_at = models.DateTimeField(blank=True, null=True)
    canceled_at = models.DateTimeField(blank=True, null=True)
    reason = models.IntegerField(blank=True, null=True)

    @staticmethod
    def to_timestamp(_datetime):
        return int(_datetime.timestamp() * 1000) if _datetime else 0

    def get_perform_time(self):
        return self.to_timestamp(self.performed_at)

    def get_canceled_time(self):
        return self.to_timestamp(self.canceled_at)

    def get_created_time(self):
        return self.to_timestamp(self.created_at)

    def __str__(self):
        return self.pk
