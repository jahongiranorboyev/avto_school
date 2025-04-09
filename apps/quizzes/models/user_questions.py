from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel


class UserQuestion(BaseModel):
    class QuestionType(models.TextChoices):
        Saved = 'saved', 'Saved'
        Correct = 'correct', 'Correct'
        Incorrect = 'incorrect', 'Incorrect'

    question = models.ForeignKey(
        'quizzes.Question',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    question_type = models.CharField(
        max_length=30,
        choices=QuestionType,
        blank=True,
        null=True
    )

    def __str__(self):
        return f" {self.user.full_name} - {self.question.title}"

    class Meta:
        unique_together = ('question', 'user','question_type')


