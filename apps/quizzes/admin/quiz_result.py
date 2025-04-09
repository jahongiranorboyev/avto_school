from django.contrib import admin
from apps.quizzes.models import QuizResult

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ("user", "correct_answers", "incorrect_answers", "total_questions")
    search_fields = ("user__username", "user__full_name")
    list_filter = ("correct_answers", "incorrect_answers")
    readonly_fields = ("total_questions",)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False