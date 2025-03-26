from django.contrib import admin
from apps.lessons.models import Lesson, Chapter
from apps.quizzes.models import QuestionCategory, Question, QuestionVariant


@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_premium', 'created_at')
    list_filter = ('is_premium', 'created_at')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('text',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'created_at')
    list_filter = ('chapter', 'created_at')
    search_fields = ('title',)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)


@admin.register(QuestionVariant)
class QuestionVariantAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')
    list_filter = ('question', 'is_correct')
    search_fields = ('text',)
