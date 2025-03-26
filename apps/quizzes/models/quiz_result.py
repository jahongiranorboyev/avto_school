from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from apps.utils.models import BaseModel
from apps.quizzes.models.question import Question


class QuizResult(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    question_category = models.ManyToManyField(
        'quizzes.QuestionCategory',
    )
    lesson = models.ForeignKey(
        'lessons.Lesson',
        on_delete=models.PROTECT,
        blank=True,
        null=True
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
        validators=[MinValueValidator(1)]
    )
    mode = models.CharField(
        max_length=10,
        choices=Question.QuestionType.choices,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Result: {self.user.full_name} )"