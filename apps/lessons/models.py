from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator

from apps.utils.models import BaseModel


class Chapter(BaseModel):
    """ This model represents a chapter of the lesson."""

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chapters/images/%Y/%m/%d', null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    lessons = models.PositiveSmallIntegerField(default=0)
    duration = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    """ This model represents a lesson for this project"""

    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='lessons/video/%Y/%m/%d', null=True, blank=True,
                             validators=[FileExtensionValidator(['mp4'])])
    description = models.TextField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    duration = models.PositiveSmallIntegerField(default=0)
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
    completed_lessons = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.id


class UserLesson(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.user.id
