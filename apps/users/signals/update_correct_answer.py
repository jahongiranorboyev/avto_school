from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.quizzes.models import QuizResult

@receiver(post_save, sender=QuizResult)
def update_users_correct_answer(sender, instance, **kwargs):
    user = instance.user

    total_correct_answers = QuizResult.objects.filter(
        user__id=user.pk).aggregate(
        total_answer=Sum('correct_answers'))['total_answer'] or 0
    user.correct_answers = total_correct_answers
    user.save(update_fields=['correct_answers'])

