
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.general.apps.GeneralConfig',
    'apps.authentications.apps.AuthenticationsConfig',
    'apps.books.apps.BooksConfig',
    'apps.lessons.apps.LessonsConfig',
    'apps.notifications.apps.NotificationsConfig',
    'apps.payments.apps.PaymentsConfig',
    'apps.phrases.apps.PhrasesConfig',
    'apps.quizzes.apps.QuizzesConfig',
    'apps.roadsigns.apps.RoadsignsConfig',
    'apps.utils.apps.UtilsConfig',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'ckeditor',
    'ckeditor_uploader',
]

INSTALLED_APPS = THIRD_PARTY_APPS + INSTALLED_APPS + MY_APPS


