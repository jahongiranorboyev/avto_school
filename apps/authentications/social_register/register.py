import os
from django.conf import settings
from django.db import transaction
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from apps.users.models import CustomUser
from apps.utils.custom_exception import CustomAPIException

@transaction.atomic()
def register_social_user(provider, email, full_name, user_code, *args, **kwargs):
    filtered_user_by_email = CustomUser.objects.filter(email=email).first()

    if filtered_user_by_email:
        try:
            if provider == filtered_user_by_email.auth_provider:
                registered_user = authenticate(
                    email=email, password = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
                )

                return {
                    'tokens': registered_user.tokens(),
                }
            else:

                raise CustomAPIException(
                    message=_('Please continue your login using ') + filtered_user_by_email.auth_provider
                )
        except CustomAPIException:
            raise CustomAPIException(message=_(f'We do not have any user in base'))
    else:
        if provider == 'telegram':
            user = {
                'email': email,
                'password': "password",
                'full_name': full_name
            }

            user = CustomUser.objects.create(**user)
            user.auth_provider = provider
            user.save()
            new_user = authenticate(
                email=email, password=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET)

            return {
                'tokens': new_user.tokens(),
            }
        else:

            user = {
                'email': email,
                'password': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                'full_name': full_name
            }

            user = CustomUser.objects.create_user(**user)
            user.auth_provider = provider
            user.save()
            new_user = authenticate(
                email=email, password=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET)

            return {
                'tokens': new_user.tokens(),
            }
