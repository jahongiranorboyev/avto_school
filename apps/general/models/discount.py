from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseModel


class Discount(BaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Name'),
    )
    amount = models.IntegerField(
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