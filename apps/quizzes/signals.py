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
