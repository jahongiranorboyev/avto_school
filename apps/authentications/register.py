import os
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from apps.users.models import CustomUser
from django.db import transaction
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

@transaction.atomic()
def register_social_user(provider, email, full_name, user_code, *args, **kwargs):
    filtered_user_by_email = CustomUser.objects.filter(email=email).first()

    if filtered_user_by_email:
        try:
            if provider == filtered_user_by_email.auth_provider:
                registered_user = authenticate(
                    email=email, password = SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
                )

                return {
                    'tokens': registered_user.tokens(),
                }
            else:

                raise AuthenticationFailed(
                    detail='Please continue your login using ' + filtered_user_by_email.auth_provider
                )
        except IndexError as e:
            raise {'error ': f'We do not have any user in base: {str(e)}'}
    else:
        if provider == 'telegram':
            user = {
                'email': email,
                'password': SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                'full_name': full_name
            }

            user = CustomUser.objects.create(**user)
            user.auth_provider = provider
            user.save()
            new_user = authenticate(
                email=email, password=SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET)

            return {
                'tokens': new_user.tokens(),
            }
        else:

            user = {
                'email': email,
                'password': SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                'full_name': full_name
            }

            user = CustomUser.objects.create_user(**user)
            user.auth_provider = provider
            user.save()
            new_user = authenticate(
                email=email, password=SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET)

            return {
                'tokens': new_user.tokens(),
            }
