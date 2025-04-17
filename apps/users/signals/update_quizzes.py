from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.quizzes.models import QuizResult


@receiver(post_save, sender=QuizResult)
def update_last_10_quiz_result(sender, instance, **kwargs):
    user = instance.user

    total_correct_answers = QuizResult.objects.filter(user=user).aggregate(
        total_answers=Sum('correct_answers'))['total_answers']

    last_10_quizzes = QuizResult.objects.all().order_by('-created_at')[:10]
    total_question = last_10_quizzes.aggregate(total_quizz=Sum('total_questions'))['total_quizz']
    if total_correct_answers:
        avg_last_10_quizz = (total_correct_answers / total_question) * 100
    else:
        avg_last_10_quizz = 0

    user.last_10_quiz_results_avg = round(avg_last_10_quizz, 2)
    user.save(update_fields=['last_10_quiz_results_avg'])
