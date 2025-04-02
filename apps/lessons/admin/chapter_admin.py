from django.utils.html import format_html
from django.contrib import admin
from apps.lessons.models.chapter import Chapter, UserChapter


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("title", "is_premium", "lessons", "duration", "image_preview")
    list_filter = ("is_premium","duration")
    search_fields = ("title",)
    ordering = ("title","created_at")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;"/>', obj.image.url)
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"


@admin.register(UserChapter)
class UserChapterAdmin(admin.ModelAdmin):
    list_display = ("user", "chapter", "completed_lessons")
    list_filter = ("chapter",)
    search_fields = ("user__username", "chapter__title")
    ordering = ("user", "chapter", "created_at")
