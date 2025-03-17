from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.validators import MinValueValidator

from apps.utils.models import BaseModel


class QuestionCategory(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    image = models.ImageField(upload_to='question_categories/%Y/%m/%d')
    is_premium = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserQuestionCategory(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    question_category = models.ForeignKey('quizzes.QuestionCategory', on_delete=models.PROTECT)
    last_quiz_results_avg = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.question_category} ({self.last_quiz_results_avg})"

    class Meta:
        unique_together = ('user', 'question_category')


class Question(BaseModel):
    class QuestionType(models.TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium'
        HARD = 'hard', 'Hard'
        EMPTY = 'empty', 'Empty'

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    mode = models.CharField(max_length=10, choices=QuestionType.choices, default=QuestionType.EMPTY)
    image = models.ImageField(upload_to='questions/%Y/%m/%d', null=True, blank=True)
    video = models.FileField(upload_to='questions/%Y/%m/%d', null=True, blank=True)
    question_category = models.ForeignKey('quizzes.QuestionCategory', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class QuestionVariant(BaseModel):
    title = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    description = models.TextField(max_length=200, null=True, blank=True)
    question = models.ForeignKey('quizzes.Question', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class SavedQuestion(BaseModel):
    question = models.ForeignKey('quizzes.Question', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"Saved: {self.user} - {self.question}"


class CorrectQuestion(BaseModel):
    question = models.ForeignKey('quizzes.Question', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"Correct: {self.user} - {self.question}"


class IncorrectQuestion(BaseModel):
    question = models.ForeignKey('quizzes.Question', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"Incorrect: {self.user} - {self.question}"


class QuizResult(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    question = models.ForeignKey('quizzes.Question', on_delete=models.PROTECT)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.PROTECT)

    correct_answers = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    incorrect_answers = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    total_questions = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])

    mode = models.CharField(max_length=10, choices=Question.QuestionType.choices, default=Question.QuestionType.EMPTY)

    def __str__(self):
        return f"Result: {self.user} - {self.question} ({self.correct_answers}/{self.total_questions})"


