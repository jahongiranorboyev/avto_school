from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseModel

class Lesson(BaseModel):
    """ This model represents a lesson for this project """

    title = models.CharField(max_length=100, verbose_name=_("Title"))
    video = models.FileField(
        upload_to='lessons/video/%Y/%m/%d',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['mp4'])]
    )
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    is_premium = models.BooleanField(default=False)
    duration = models.PositiveSmallIntegerField(default=0)
    chapter = models.ForeignKey('lessons.Chapter', on_delete=models.PROTECT, related_name='chapter_lessons')

    def __str__(self):
        return self.title


class LessonResource(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    url = models.URLField(null=True, blank=True)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class LessonTerm(BaseModel):
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class UserLesson(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.PROTECT)
    completed_at = models.DateTimeField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return str(self.user.id)
