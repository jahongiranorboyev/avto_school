import os
from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('uz', _('Uzbek')),
    ('ru', _('Russian')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'uz'

# Static and Media
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'users.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Payme ID and Key
PAYME_CASH_BOX_ID = os.environ.get("PAYME_CASH_BOX_ID")
PAYME_CASH_BOX_TEST_KEY = os.environ.get("PAYME_CASH_BOX_TEST_KEY")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


EMAIL_BACKEND = 'd  jango.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hikmatovsanjar885@gmail.com'
EMAIL_HOST_PASSWORD = 'ubmb kdxt mmgu vgbt'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


CORS_ALLOWED_ORIGINS = [
    'https://5e69-90-156-198-203.ngrok-free.app'
]