from modeltranslation.translator import register, TranslationOptions
from .models import Question, QuestionVariant, QuestionCategory


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(QuestionVariant)
class QuestionVariantTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(QuestionCategory)
class QuestionCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)



