from django.contrib import admin
from apps.quizzes.models import UserQuestion

@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('user__full_name', 'question__title', 'question_type')
    list_filter = ('question_type', 'user__full_name')
    search_fields = ('user__full_name', 'question__title')
    ordering = ('user__full_name', 'question_type')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False