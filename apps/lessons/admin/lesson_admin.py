from django.contrib import admin
from apps.lessons.models import Lesson, LessonTerm, UserLesson,LessonResource

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "is_premium", "duration", "chapter")
    list_filter = ("is_premium", "chapter")
    search_fields = ("title", "description")
    ordering = ("chapter", "title")

@admin.register(LessonResource)
class LessonResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "lesson")
    list_filter = ("lesson",)
    search_fields = ("title", "url")

@admin.register(LessonTerm)
class LessonTermAdmin(admin.ModelAdmin):
    list_display = ("name", "lesson")
    list_filter = ("lesson",)
    search_fields = ("name", "description")

@admin.register(UserLesson)
class UserLessonAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "completed_at", "rating")
    list_filter = ("lesson", "rating")
    search_fields = ("user__username", "lesson__title")
    ordering = ("-completed_at",)
