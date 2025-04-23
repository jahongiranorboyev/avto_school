# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
from django.conf import settings

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': settings.BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_avto',
        'USER': 'user_avto',
        'PASSWORD': 1,
        'HOST': 'my_avto_db',
        'PORT': '5432',
    }
}


