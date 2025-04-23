import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = 'hikmatovsanjar885@gmail.com'
EMAIL_HOST_PASSWORD = 'ubmb kdxt mmgu vgbt'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
