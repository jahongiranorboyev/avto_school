from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from apps.utils.models import BaseModel


class QuizResult(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    correct_answers = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    incorrect_answers = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    total_questions = models.IntegerField(
        editable=False,
        default= 0,
        validators=[MinValueValidator(1)]
    )
    def save(self,*args,**kwargs):
        self.total_questions = self.correct_answers + self.incorrect_answers
        super().save(*args,**kwargs)


    def __str__(self):
        return f"Result: {self.user.full_name} )"