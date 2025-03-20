from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.validators import MinValueValidator, FileExtensionValidator
from rest_framework.exceptions import ValidationError

from apps.utils.models import BaseModel
from django.db.models import Avg, F, FloatField, UniqueConstraint


class QuestionCategory(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        editable=False,
    )
    image = models.ImageField(upload_to='question_categories/%Y/%m/%d')
    is_premium = models.BooleanField(default=False, editable=False)

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)

        if QuestionCategory.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError("A question category with this slug already exists")

    def __str__(self):
        return self.title


class UserQuestionCategory(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    question_category = models.ForeignKey(
        'quizzes.QuestionCategory',
        on_delete=models.PROTECT
    )
    last_quiz_results_avg = models.FloatField(
        editable=False,
        null=True,
        blank=True
    )

    def update_last_quiz_results_avg(self):
        last_10_results = (
            QuizResult.objects
            .filter(user=self.user, question_category=self.question_category)
            .order_by("-created_at")[:10]
        )
        aggregated_data = last_10_results.aggregate(
            avg_correct=Avg(
                F("correct_answers") * 100.0 / F("total_questions"),
                output_field=FloatField()
            )
        )

        self.last_quiz_results_avg = aggregated_data["avg_correct"] or 0.0
        self.save()

    def __str__(self):
        return f"{self.user.full_name} - {self.question_category.title}"

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'question_category'],
                             name='unique_user_question_category')
        ]


class Question(BaseModel):
    class QuestionType(models.TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium'
        HARD = 'hard', 'Hard'
        EMPTY = 'empty', 'Empty'

    question_category = models.ForeignKey(
        'quizzes.QuestionCategory',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        'lessons.Lesson',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        editable=False
    )
    mode = models.CharField(
        max_length=10,
        choices=QuestionType.choices,
        default=QuestionType.EMPTY
    )
    video = models.FileField(
        upload_to='questions/%Y/%m/%d',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    image = models.ImageField(
        upload_to='questions/%Y/%m/%d',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ]
    )

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)

        if Question.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError("A question  with this slug already exists")

        if not self.lesson and not self.question_category:
            raise ValidationError("Either 'lesson' or 'question_category' must be provided.")

    def __str__(self):
        return self.title


class QuestionVariant(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        editable=False
    )
    is_correct = models.BooleanField(
        default=False,
        editable=False
    )
    description = models.TextField(max_length=200)
    question = models.ForeignKey(
        'quizzes.Question',
        on_delete=models.PROTECT
    )

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)

        if QuestionVariant.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError("A question Variant  with this slug already exists")

    def __str__(self):
        return self.title


class SavedQuestion(BaseModel):
    question = models.ForeignKey(
        'quizzes.Question',
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Saved: {self.user.full_name} - {self.question.title}"

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'question'],
                             name='unique_saved_question')
        ]


class CorrectQuestion(BaseModel):
    question = models.ForeignKey(
        'quizzes.Question',
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Correct: {self.user.full_name} - {self.question.title}"

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'question'],
                             name='unique_correct_question')
        ]

class IncorrectQuestion(BaseModel):
    question = models.ForeignKey(
        'quizzes.Question',
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Incorrect: {self.user.full_name} - {self.question.title}"

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'question'],
                             name='unique_incorrect_question')
        ]

class QuizResult(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    question_category = models.ManyToManyField(
        'quizzes.QuestionCategory',
        blank=True
    )
    lesson = models.ForeignKey(
        'lessons.Lesson',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    correct_answers = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]
    )
    incorrect_answers = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]
    )
    total_questions = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)]
    )
    mode = models.CharField(
        max_length=10,
        choices=Question.QuestionType.choices,
        default=Question.QuestionType.EMPTY
    )

    def __str__(self):
        return f"Result: {self.user.full_name} )"
