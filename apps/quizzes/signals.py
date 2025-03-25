<<<<<<< HEAD
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QuizResult, UserQuestionCategory

@receiver(post_save, sender=QuizResult)
def user_question_category_post_save(sender, instance, created, **kwargs):
    if created:
        for category in instance.question_category.all():
            user_category, _ = UserQuestionCategory.objects.get_or_create(
                user=instance.user, question_category=category
            )
            user_category.update_last_quiz_results_avg()
=======
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from apps.quizzes.models import QuizResult, UserQuestionCategory


@receiver(post_save, sender=QuizResult)
def update_user_question_category(sender, instance, created, **kwargs):
    """
    When a new QuizResult is created, update UserQuestionCategory's last_quiz_results_avg.
    """
    if instance.total_questions and instance.correct_answers is not None:
        correct_percentage = (instance.correct_answers / instance.total_questions) * 100

        user_category, _ = UserQuestionCategory.objects.get_or_create(
            user=instance.user,
            question_category=instance.question.question_category
        )

        if user_category.last_quiz_results_avg:
            user_category.last_quiz_results_avg = (user_category.last_quiz_results_avg + correct_percentage) / 2
        else:
            user_category.last_quiz_results_avg = correct_percentage

        user_category.save()


@receiver(pre_delete, sender=QuizResult)
def handle_quiz_result_deletion(sender, instance, **kwargs):
    """
    If a QuizResult is deleted, recalculate the UserQuestionCategory's last_quiz_results_avg.
    """
    user_category = UserQuestionCategory.objects.filter(
        user=instance.user,
        question_category=instance.question.question_category
    ).first()

    if user_category:
        all_results = QuizResult.objects.filter(
            user=instance.user,
            question__question_category=instance.question.question_category
        ).exclude(id=instance.id)

        if all_results.exists():
            new_avg = sum((r.correct_answers / r.total_questions) * 100 for r in all_results) / all_results.count()
            user_category.last_quiz_results_avg = new_avg
        else:
            user_category.last_quiz_results_avg = None
        user_category.save()
>>>>>>> b6888bd (quizzes done !)
