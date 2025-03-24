from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

from apps.utils.models import BaseModel


class Discount(BaseModel):
    name = models.CharField(
        max_length=500,
        verbose_name=_('Name'),
    )
    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name=_('Amount'),
    )
    is_percent = models.BooleanField(
        default=False,
        verbose_name=_('Is percent'),
    )


    def __str__(self):
        return self.name