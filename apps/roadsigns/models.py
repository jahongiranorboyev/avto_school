from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.utils.models import BaseModel

class RoadSign(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to="roadsigns/images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name=_('Image'),
    )
    parent = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Parent'),
    )
    ordering = models.IntegerField(
        default=0,
        verbose_name=_('Ordering'),
    )
    class Meta:
        unique_together = ( 'parent','ordering' )

    def __str__(self):
        return self.title
