from apps.users.models import CustomUser
from modeltranslation.translator import translator, TranslationOptions

class CustomUserTranslationOptions(TranslationOptions):
    fields = ('full_name', 'first_name')

translator.register(CustomUser, CustomUserTranslationOptions)
