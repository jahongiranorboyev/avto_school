from rest_framework.response import Response
from apps.authentications.google import Google
import os
from django.shortcuts import render
from rest_framework.decorators import api_view
from apps.authentications.register import register_social_user

def google(request):
    return render(request=request, template_name='google_login.html')

@api_view(['POST'])
def google_auth_token(request):
    """
    Google tokenini dekodlash va foydalanuvchini aniqlash
    """
    id_token = request.data.get('id_token')

    user_data = Google.validate(id_token)
    try:
        user_data['sub']
    except KeyError:
        raise ValueError({'error': 'The token is invalid or expired. Please login again'})

    if user_data['aud'] != os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'):
        raise ValueError('oops who are you')

    user_id = user_data['sub']
    email = user_data['email']
    name = user_data['name']
    user_code = user_data.get('user_code', '')
    provider = 'google'

    user = register_social_user(provider=provider, user_id=user_id, email=email, full_name=name,
                                user_code=user_code)

    return Response({"message": "User successfully authenticated", "user": user.id})
