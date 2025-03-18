import random

from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings


class Email:
    @staticmethod
    def send_massage(email):

        code = random.randint(000000, 999999)

        cache.set(f'user_code_{email}', code, timeout=2 * 60)
        cache.set(f'user_email_{code}', email, timeout=2 * 60)

        if email:
            subject = "Welcome to Online Auto School!"
            message = f'it is your code enter the code: {code}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

email_service = Email()