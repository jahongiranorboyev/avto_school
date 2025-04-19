from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

from apps.general.views.custom_xception import CustomAPIException
from apps.quizzes.models import Question, QuestionVariant


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
            raise CustomAPIException(_("Each question must have at least 2 options."))
        if correct_answers != 1:
            raise CustomAPIException(_("Each question should have only 1 correct answer."))

class QuestionVariantInline(admin.TabularInline):
    model = QuestionVariant
    extra = 1
    formset = QuestionVariantInlineFormset


class QuestionAdmin(TranslationAdmin):
    list_display = ('title', 'mode', 'question_category', 'lesson', 'get_variants')
    search_fields = ('title', 'description')
    list_filter = ('mode', 'question_category', 'lesson')
    readonly_fields = ('is_saved',)
    inlines = [QuestionVariantInline]

    def get_variants(self, obj):
        return ", ".join([variant.title for variant in obj.variants.all()])

    get_variants.short_description = 'Variants'


class QuestionVariantAdmin(TranslationAdmin):
    list_display = ('title', 'is_correct', 'question')
    list_filter = ('is_correct',)


# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionVariant, QuestionVariantAdmin)
