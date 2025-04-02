from django.dispatch import receiver
from .models.lesson import UserLesson,Lesson
from django.db.models.signals import post_save,post_delete


@receiver(post_save, sender=UserLesson)
def add_coin_when_userlesson_created(sender, instance, created, **kwargs):
    """  if UserLesson created then user's coin added one coin for completed lesson"""

    if created:
        instance.user.coins += 1
        instance.user.save()

@receiver(post_save, sender=Lesson)
def update_lesson_count_on_save(sender, instance, created, **kwargs):
    """ if lesson created then chapter lesson count increased one"""
    if created:
        chapter = instance.chapter
        chapter.lessons += 1
        chapter.save()


@receiver(post_delete, sender=Lesson)
def update_lesson_count_on_delete(sender, instance, **kwargs):
    """ if lesson deleted then chapter lesson count decreased one"""
    chapter = instance.chapter
    if chapter.lessons > 0:
        chapter.lessons -= 1
        chapter.save()

