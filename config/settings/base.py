import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from django.conf.global_settings import STATIC_ROOT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# INSTALLED_APPS
# config/settings/installed_apps

# Database
# config/settings/databases

# Password validation
# config/settings/auth_password_validators

# MIDDLEWARE
# config/settings/middleware

# TEMPLATES
# config/settings/templates

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = 'hsrf bhwa iehf aoaw'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

