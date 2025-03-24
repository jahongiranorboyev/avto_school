from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseModel


class Report(BaseModel):
    class ReportType(models.TextChoices):
        TYPO = 'typo', _('Typo')
        DONTUNDERSTAND = 'dontunderstand', _('Dontunderstand')
        IMAGEVIDEO = 'image_video', _('Image Video')
        FACTUALERROR = 'factual_error', _('Factual Error')
        OTHER = 'other', _('Other')


    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            verbose_name=_('User'),
    )
    lesson = models.ForeignKey(
        to='lessons.Lesson',
        on_delete=models.PROTECT,
        verbose_name=_('Lesson'),
    )
    question = models.ForeignKey(
        to='quizzes.Question',
        on_delete=models.PROTECT,
        verbose_name=_('Question'),
    )
    report_type = models.CharField(
        max_length=100,
        choices=ReportType.choices,
        verbose_name=_('Report type'),
    )
    reason = models.CharField(
        max_length=100,
        verbose_name=_('Reason'),
    )

    def __str__(self):
        return self.question.title