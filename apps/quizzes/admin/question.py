from django.contrib import admin

from apps.quizzes.models import Question, QuestionVariant

class QuestionVariantInline(admin.TabularInline):
    model = QuestionVariant
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'mode', 'question_category', 'lesson', 'get_variants')
    search_fields = ('title', 'description')
    list_filter = ('mode', 'question_category', 'lesson')

    def get_variants(self, obj):
        return ", ".join([variant.title for variant in obj.variants.all()])


    get_variants.short_description = 'Variants'
    inlines = [QuestionVariantInline]

class QuestionVariantAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_correct', 'question')
    list_filter = ('is_correct',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionVariant, QuestionVariantAdmin)
