from django.db import models

from apps.utils.models import BaseModel


class OrderItem(BaseModel):

    user = models.ForeignKey('users.CustomUser', on_delete=models.PROTECT)
    order = models.ForeignKey('payments.Order', on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)