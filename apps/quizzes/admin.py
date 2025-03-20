from django.contrib import admin
from rest_framework.exceptions import ValidationError

from .models import (
    QuestionCategory, UserQuestionCategory, Question,
    QuestionVariant, SavedQuestion, CorrectQuestion,
    IncorrectQuestion, QuizResult
)

@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_premium", "created_at")
    search_fields = ("title",)
    readonly_fields = ("slug", "created_at", "updated_at")

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "mode", "question_category", "created_at")
    search_fields = ("title",)
    list_filter = ("mode", "question_category")
    readonly_fields = ("slug", "created_at", "updated_at")

@admin.register(UserQuestionCategory)
class UserQuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ("user", "question_category", "last_quiz_results_avg", "created_at")
    search_fields = ("user__username", "question_category__title")

@admin.register(QuestionVariant)
class QuestionVariantAdmin(admin.ModelAdmin):
    list_display = ("title", "is_correct", "question", "created_at")
    list_filter = ("is_correct",)

@admin.register(SavedQuestion)
class SavedQuestionAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "created_at")

@admin.register(CorrectQuestion)
class CorrectQuestionAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "created_at")

@admin.register(IncorrectQuestion)
class IncorrectQuestionAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "created_at")

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ("user", "correct_answers", "incorrect_answers", "total_questions", "mode", "created_at")
    list_filter = ("mode",)
    search_fields = ("user__fullname",)
