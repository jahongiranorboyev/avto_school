from django.db.models import Sum, F, Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.quizzes.models import QuizResult, Question
from apps.users.models import CustomUser


#
# @receiver(post_save, sender=QuizResult)
# def update_users_correct_answers(sender, instance, created, **kwargs):
#
#     user = instance.user
#
#
#     if user:
#         total_correct_answers = QuizResult.objects.filter(user=user).aggregate(total_answere=Sum('correct_answers'))['total_answere'] or 0
#         user.correct_answers = total_correct_answers
#         user.save(update_fields=['correct_answers'])


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


@receiver(post_save, sender=QuizResult)
def update_users_correct_answer(sender, instance, **kwargs):
    user = instance.user

    total_correct_answers = QuizResult.objects.filter(
        user__id=user.pk).aggregate(
        total_answer=Sum('correct_answers'))['total_answer'] or 0
    user.correct_answers = total_correct_answers


# @receiver(post_save, sender=CustomUser)
# def update_user_level(sender, instance, **kwargs):
#