from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel


class Chapter(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chapters/', null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    lessons = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='lessons/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    duration = models.IntegerField(default=0)
    chapter = models.ForeignKey('lessons.Chapter', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LessonResource(BaseModel):
    title = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LessonTerm(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserChapter(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chapter = models.ForeignKey('lessons.Chapter', on_delete=models.CASCADE)
    completed_lessons = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class UserLesson(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True, blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.id
