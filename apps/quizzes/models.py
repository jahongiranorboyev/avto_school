from django.conf import settings
from django.db import models
from apps.utils.models import BaseModel


class QuestionCategory(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='question_categories')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class UserQuestionCategory(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question_category = models.ForeignKey('quizzes.QuestionCategory', on_delete=models.CASCADE)
    last_quize_results_avg = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.last_quize_results_avg

class Question(BaseModel):
    title = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    image = models.ImageField(upload_to='questions')
    video = models.FileField(upload_to='questions')
    question_category = models.ForeignKey('quizzes.QuestionCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class QuestionVariant(BaseModel):
    title = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    question = models.ForeignKey('quizzes.Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SavedQuestion(BaseModel):
    question = models.ForeignKey('quizzes.Question', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title

class CorrectQuestion(BaseModel):
    question = models.ForeignKey('quizzes.Question', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title

class IncorrectQuestion(BaseModel):
    question = models.ForeignKey('quizzes.Question', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title

class QuizeResult(BaseModel):
    question = models.ForeignKey('quizzes.Question', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    correct_answers = models.IntegerField(null=True, blank=True)
    incorrect_answers = models.IntegerField(null=True, blank=True)
    total_questions = models.IntegerField(null=True, blank=True)
    mode = models.CharField(max_length=100)

    def __str__(self):
        return self.question.title
