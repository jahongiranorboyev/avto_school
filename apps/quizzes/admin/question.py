from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from apps.quizzes.models import Question, QuestionVariant


# Custom formset for validation inside the admin
class QuestionVariantInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        total_forms = 0
        correct_answers = 0

        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                total_forms += 1
                if form.cleaned_data.get('is_correct', False):
                    correct_answers += 1

        if total_forms < 2:
            raise ValidationError("Har bir savol kamida 2 ta variantga ega bo'lishi kerak.")
        if correct_answers != 1:
            raise ValidationError("Har bir savolda faqat 1 ta to'g'ri javob bo'lishi kerak.")


# Inline form with the custom formset
class QuestionVariantInline(admin.TabularInline):
    model = QuestionVariant
    extra = 1
    formset = QuestionVariantInlineFormset


# Admin for Question model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'mode', 'question_category', 'lesson', 'get_variants')
    search_fields = ('title', 'description')
    list_filter = ('mode', 'question_category', 'lesson')
    readonly_fields = ('is_saved',)
    inlines = [QuestionVariantInline]

    def get_variants(self, obj):
        return ", ".join([variant.title for variant in obj.variants.all()])

    get_variants.short_description = 'Variants'


# Admin for QuestionVariant model
class QuestionVariantAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_correct', 'question')
    list_filter = ('is_correct',)


# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionVariant, QuestionVariantAdmin)
