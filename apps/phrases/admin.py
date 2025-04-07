from django.contrib import admin
from apps.phrases.models import Phrase, UserCompletedPhrase


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("title",)
    search_fields = ("title", "description")
    ordering = ("created_at", )


@admin.register(UserCompletedPhrase)
class UserCompletedPhraseAdmin(admin.ModelAdmin):
    list_display = ("user__full_name", "phrase__title" )
    list_filter = ("user__full_name", "phrase__title")
    search_fields = ("user__name", "phrase__description")
    ordering = ("created_at", )
