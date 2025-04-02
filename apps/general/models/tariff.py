from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseModel


class Tariff(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )
    days = models.IntegerField(
        default=0,
        verbose_name=_('Days'),
    )
    price = models.IntegerField(
        default=0,
        verbose_name=_('Price'),
    )
    discount = models.ForeignKey(
        to='general.Discount',
        on_delete=models.PROTECT,
        verbose_name=_('Discount'),
    )

    def __str__(self):
        return self.title