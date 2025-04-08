from django.contrib import admin
from apps.quizzes.models import QuestionCategory

@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "question_count", "is_premium")
    search_fields = ("title",)
    list_filter = ("is_premium",)
    readonly_fields = ("question_count",)
