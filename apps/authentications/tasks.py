from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import logging

from apps.utils.custom_exception import CustomAPIException

logger = logging.getLogger(__name__)



def send_verification_code_email(email, code, purpose):
    if email is None:
        raise CustomAPIException(message={'error': _('Email is required')})

    try:
        if purpose == 'verify':
            subject = _("Confirm your registration")
            action_link = f"http://127.0.0.1:8000/api/v1/auth/register-verify-code/?code={code}&email={email}"
            action_text = _("Confirm Registration")
            description = _("To complete your registration, please click the button below:")
        elif purpose == 'reset':
            subject = _("Password reset link")
            action_link = f"http://127.0.0.1:8000/api/v1/auth/forget-password-verify-code/?code={code}&email={email}"
            action_text = _("Reset Password")
            description = _("To reset your password, please click the button below:")
        else:
            raise CustomAPIException(message={'error': _('Invalid email purpose')})

        from_email = settings.DEFAULT_FROM_EMAIL

        reply_to = [email]
        logo_text = _("Online Auto School")
        animated_logo = "".join(
            f'<span style="display: inline-block; animation: pulse {0.6 + i*0.1}s ease-in-out infinite, colorChange {1.2 + i*0.15}s infinite;">{char}</span>'
            for i, char in enumerate(logo_text)
        )

        context = {
            'animated_logo': animated_logo,
            'subject': subject,
            'description': description,
            'action_link': action_link,
            'action_text': action_text,
            'from_email': from_email,
            'code': code,
        }

        html_content = render_to_string('emails/verification_email.html', context)

        msg = EmailMultiAlternatives(subject, "", from_email, reply_to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Exception as e:
        logger.error(f"Email yuborishda xatolik: {e}")
        raise CustomAPIException(message={'error': _('Failed to send email. Please try again later.')})
