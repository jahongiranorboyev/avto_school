from django.db import models
from rest_framework.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from apps.utils.models import BaseModel
from apps.utils.services.quizzes.check_image import validate_image
from apps.utils.services.quizzes.check_video import validate_video


class Question(BaseModel):
    class QuestionType(models.TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium'
        HARD = 'hard', 'Hard'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    mode = models.CharField(
        max_length=10,
        choices=QuestionType.choices,

    )
    video = models.FileField(
        upload_to='questions/%Y/%m/%d',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4']),
            validate_video
        ]
    )
    image = models.ImageField(
        upload_to='questions/%Y/%m/%d',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp', 'gif', 'svg', 'bmp', 'tiff']),
            validate_image
        ]
    )

    question_category = models.ForeignKey(
        'quizzes.QuestionCategory',
        on_delete=models.PROTECT
    )
    lesson = models.ForeignKey(
        'lessons.Lesson',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )


    def __str__(self):
        return self.title


class QuestionVariant(BaseModel):
    title = models.CharField(max_length=100)
    is_correct = models.BooleanField(
        default=False,
    )
    question = models.ForeignKey(
        'quizzes.Question',
        on_delete=models.PROTECT,
        related_name='variants',
    )
        
    def clean(self):
        if self.is_correct:
            existing_correct = QuestionVariant.objects.filter(
                question=self.question, is_correct=True
            ).exclude(id=self.id).exists()
            if existing_correct:
                raise ValidationError("This question already has a correct answer!")

    def __str__(self):
        return self.title

