from django.contrib import admin

from apps.utils.models import CustomLanguage


@admin.register(CustomLanguage)
class CustomLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'ordering')