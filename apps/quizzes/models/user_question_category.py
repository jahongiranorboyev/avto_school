from django.db import models
from django.conf import settings
from django.db.models import Avg,F,FloatField

from apps.utils.models import BaseModel
from apps.quizzes.models.quiz_result import QuizResult


class UserQuestionCategory(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    question_category = models.ForeignKey(
        'quizzes.QuestionCategory',
        on_delete=models.PROTECT
    )
    last_quiz_results_avg = models.FloatField(
        editable=False,
        default=0
    )

    def update_last_quiz_results_avg(self):
        last_10_results = (
            QuizResult.objects
            .filter(user=self.user, question_category=self.question_category)
            .order_by("-created_at")[:10]
        )

        aggregated_data = last_10_results.aggregate(
            avg_correct=Avg(
                F("correct_answers") * 100.0 / F("total_questions"),
                output_field=FloatField()
            )
        )
        self.last_quiz_results_avg = aggregated_data["avg_correct"] or 0.0
        self.save()

    def __str__(self):
        return f"{self.user.full_name} - {self.question_category.title}"

    class Meta:
        unique_together = ("user", "question_category")
