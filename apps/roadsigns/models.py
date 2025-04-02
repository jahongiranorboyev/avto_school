from django.db import models

from apps.utils.models import BaseModel
from apps.general.validation_image import check_image


class RoadSign(BaseModel):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField(
        max_length=5000
    )
    image = models.ImageField(
        upload_to="roadsigns/images/%Y/%m/%d/",
        validators=[check_image],
        null=True,
        blank=True,
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    ordering = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.title
