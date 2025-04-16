from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseModel


class Chapter(BaseModel):
    """ This model represents a chapter of the lesson. """

    title = models.CharField(max_length=100, verbose_name=_("Title"))
    image = models.ImageField(upload_to='chapters/images/%Y/%m/%d', null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    lessons = models.PositiveSmallIntegerField(default=0)
    duration = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title


class UserChapter(BaseModel):
    """ This model represents how many lessons of chapter finished by user. """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    chapter = models.ForeignKey('lessons.Chapter', on_delete=models.PROTECT)
    completed_lessons = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.id
