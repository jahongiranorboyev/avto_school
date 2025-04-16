from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.quizzes.models import Question

def update_question_category_count(category):
    category.question_count = Question.objects.filter(question_category_id=category.pk).count()
    category.save()

@receiver(post_save, sender=Question)
def post_save_question(sender, instance, created, **kwargs):
    update_question_category_count(instance.question_category)

@receiver(post_delete, sender=Question)
def post_delete_question(sender, instance, **kwargs):
    update_question_category_count(instance.question_category)


