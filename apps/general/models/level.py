from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseModel
from apps.general.validation_image import check_image


class Level(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )
    icon = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_('Icon'),
        upload_to='icons/images/%Y/%m/%d/',
        validators=[check_image],

    )
    coins = models.IntegerField(
        default=0,
        verbose_name=_('Coins'),
    )

    def __str__(self):
        return self.title