from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_verification_code_email(email, code):
    if email:
        try:
            subject = "Welcome to Online Auto School!"
            message = f"It is your code, enter the code: {code}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

        except Exception as e:
            raise ValueError({'error': f'Our random code generator not working {e}'})

    else:
        raise ValueError({'error': 'Email required'})

