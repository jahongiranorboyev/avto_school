from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _, get_language

from apps.utils.models import BaseModel


class Report(BaseModel):
    class ReportChoices(models.TextChoices):
        TOPY = 'topy',_('Topy')
        DONTUNDERSTAND = 'dontunderstand',_('Dontunderstand')
        IMAGE_VEDO = 'image-vedo',_('Image vedo')
        FACTUAL_EROR = 'face-error',_('Face error')
        OTHERS = 'others',_('Others')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )
    lesson = models.ForeignKey(
        to='lessons.Lesson',
        on_delete=models.CASCADE,
        verbose_name=_('Lesson'),
    )
    question = models.ForeignKey(
        to='quizzes.Question',
        on_delete=models.CASCADE,
        verbose_name=_('Question'),
    )
    report_type = models.CharField(
        max_length=100,
        choices= ReportChoices.choices,
        default=ReportChoices.TOPY,
    )
    reason = models.CharField(
        max_length=100,
        verbose_name=_('Reason'),
    )

    def __str__(self):
        return self.question.title