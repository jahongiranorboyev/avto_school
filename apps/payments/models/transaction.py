from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseModel


class Transaction(BaseModel):
    class State(models.IntegerChoices):
        AWAITING_PAYMENT = 1
        COMPLETED = 2
        DOES_NOT_EXIST = -1
        CANCELLED = -2

    state = models.IntegerField(choices=State, default=State.AWAITING_PAYMENT)
    order = models.ForeignKey(to='payments.Order', on_delete=models.CASCADE)

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
        return f'{self.pk}'