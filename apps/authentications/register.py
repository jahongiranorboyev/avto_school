import os
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from apps.users.models import CustomUser




def register_social_user(provider, user_id, email, full_name, user_code):
    filtered_user_by_email = CustomUser.objects.filter(email=email).exists()

    if filtered_user_by_email:
        existing_user = filtered_user_by_email[0].first
        if provider == existing_user.auth_proveder:
            registered_user = authenticate(
                email=email, password = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
            )

            return {
                'tokens': registered_user.tokens(),
            }
        else:

            raise AuthenticationFailed(
                detail='Please continue your login using ' + existing_user.auth_provider
            )

    else:

        if provider == 'telegram':
            user = {
                'email': email,
                'password': os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'),
                'full_name': full_name
            }

            user = CustomUser.objects.create(**user)
            user.auth_provider = provider
            user.save()
            new_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'))

            return {
                'tokens': new_user.tokens(),
            }

        user = {
            'email': email,
            'password': os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'),
            'full_name': full_name
        }

        user = CustomUser.objects.create(**user)
        user.auth_provider = provider
        user.save()
        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'))

        return {
            'tokens': new_user.tokens(),
        }



