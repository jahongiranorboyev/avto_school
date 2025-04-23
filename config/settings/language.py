from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en'

USE_I18N = True
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

MODELTRANSLATION_LANGUAGE = ('uz', 'en', 'ru')

LANGUAGES = [
    ('uz', _('Uzbek')),
    ('en', _('English')),
    ('ru', _('Russian')),
]