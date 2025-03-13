from .models import UserLesson
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=UserLesson)
def add_coin_when_userlesson_created(sender, instance, created, **kwargs):
    if created: # if UserLesson created then user's coin added one coin for completed lesson
        instance.user.coins += 1

        instance.user.save()
