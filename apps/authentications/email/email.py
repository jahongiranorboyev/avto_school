import  random

from django.core.cache import cache
from apps.authentications.tasks import send_verification_code_email


class Email:
    @staticmethod
    def send_massage(email, purpose, code=None):
        """
           Sends a verification code to the user's email.
           1. Generates a random 6-digit verification code.
           2. Stores the code in the cache with the key `user_code_{email}` for 1 hour.
           3. Stores the email with the key `user_email_{code}` for reverse lookup.
           4. Sends the verification code via email along with its purpose.
        """
        code = random.randint(000000, 999999)
        # code = 123456
        cache.set(f'user_code_{email}', code, timeout=60 * 60)
        cache.set(f'user_email_{code}', email, timeout=60 * 60)

        send_verification_code_email.delay(email=email, code=code, purpose=purpose)


email_service = Email()