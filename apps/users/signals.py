from django.db.models import Sum, F, Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.general.models import Level
from apps.quizzes.models import QuizResult, Question
from apps.users.models import CustomUser



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
    user.save(update_fields=['correct_answers'])

#
# @receiver(post_save)
# def update_user_level(sender, instance, **kwargs):
#     if isinstance(instance, CustomUser):
#         levels = Level.objects.order_by('coins')
#         if not levels.exists():
#             return
#
#         for level in levels:
#             if instance.coins < level.coins:
#                 break
#             instance.level = level
#
#         instance.save(update_fields=['level'])
#
#     elif isinstance(instance, Level):
#         levels = Level.objects.order_by('coins')
#         users = CustomUser.objects.all()
#
#         for user in users:
#             for level in levels:
#                 if user.coins < level.coins:
#                     break
#                 user.level = level
#             user.save(update_fields=['level'])
#


@receiver(post_save, dispatch_uid="update_user_level")
def update_user_level(sender, instance, **kwargs):
    if isinstance(instance, CustomUser):
        post_save.disconnect(update_user_level, sender=CustomUser)

        try:
            levels = Level.objects.order_by('coins')
            if not levels.exists():
                return

            for level in levels:
                if instance.coins < level.coins:
                    break
                instance.level = level

            CustomUser.objects.filter(pk=instance.pk).update(level=instance.level)
        finally:
            post_save.connect(update_user_level, sender=CustomUser, dispatch_uid="update_user_level")

    elif isinstance(instance, Level):
        post_save.disconnect(update_user_level, sender=Level)

        try:
            levels = Level.objects.order_by('coins')
            users = CustomUser.objects.all()

            for user in users:
                for level in levels:
                    if user.coins < level.coins:
                        break
                    user.level = level
                CustomUser.objects.filter(pk=user.pk).update(level=user.level)
        finally:
            post_save.connect(update_user_level, sender=Level, dispatch_uid="update_user_level")