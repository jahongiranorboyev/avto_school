import random

from django.core.cache import cache
from apps.authentications.tasks import send_verification_code_email

class Email:
    @staticmethod
    def send_massage(email):

        # code = random.randint(000000, 999999)
        code = 123456
        cache.set(f'user_code_{email}', code, timeout=2 * 60)
        cache.set(f'user_email_{code}', email, timeout=2 * 60)

        send_verification_code_email.delay(email, code)


email_service = Email()