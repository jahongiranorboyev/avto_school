import os
import random
import string
import time

from apps.users.models import CustomUser

from rest_framework import serializers
from rest_framework_simplejwt.exceptions import AuthenticationFailed


from apps.authentications import google
from apps.users.serializers import LevelSerializer
from apps.authentications.register import register_social_user


def generate_reset_code():
    """ random code generate for send to user when user forget and"""
    exists_code = set(CustomUser.objects.values_list('user_code', flat=True))
    while True:
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choices(characters, k=8))
        if code not in exists_code:
            return code

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '603070947700-uhru8mm50534bfm6s1q0ofnlu2lh4hm8.apps.googleusercontent.com'

class GoogleSocialAuthSerializer(serializers.Serializer):
    id_token = serializers.CharField()

    def validate_auth_token(self, id_token):
        """
        Google tokenini dekodlash va foydalanuvchini aniqlash
        """
        user_data = google.Google.validate(id_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                {'error': 'The token is invalid or expired. Please login again'}
            )
        if 'error' in user_data:
            raise ValueError({'error': 'this just error i do not what happen'})

        if user_data.get('iss') not in ["https://accounts.google.com", "accounts.google.com"]:
            raise ValueError({'error': 'Invalid token issuer'})

        if user_data['aud'] != SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and user_data.get('azp') != SOCIAL_AUTH_GOOGLE_OAUTH2_KEY:
            raise AuthenticationFailed(f'oops who are you {user_data['aud']} != {SOCIAL_AUTH_GOOGLE_OAUTH2_KEY} >> {user_data.get('azp')}')

        current_time = int(time.time())
        if user_data.get("exp") < current_time:
            raise ValueError({'error': 'Token has expired'})

        email = user_data['email']
        name = user_data['name']
        user_code = generate_reset_code()
        provider = 'google'
        data = {
            'provider':provider,
            'email':email,
            'full_name':name,
            'user_code':user_code}
        return data


    def create(self, validated_data):
        id_token = validated_data.get("id_token")
        data = self.validate_auth_token(id_token)
        user = register_social_user(**data)
        return user

#
#
#
# class UserListSerializer(serializers.ModelSerializer):
#     level = LevelSerializer()
#     class Meta:
#         model = CustomUser
#         fields = '__all__'




#
#     def validate(self, data):
#         """
#         Google’dan kelgan foydalanuvchi ma’lumotlarini qaytarish
#         """
#         auth_token = data.get("auth_token")
#         user_data = self.validate_auth_token(auth_token)
#
#         email = user_data.get("email")
#         first_name = user_data.get("given_name", None)
#         last_name = user_data.get("family_name", None)
#
#         if not email:
#             raise serializers.ValidationError("Google orqali email olinmadi.")
#
#         user, created = CustomUser.objects.get_or_create(email=email, defaults={
#             "first_name": first_name,
#             "google_id": user_data.get("sub"),
#             "is_active": True
#         })
#
#         data["user"] = user
#         data["is_new_user"] = created
#         return data
#
# class RegisterSerializer(serializers.ModelSerializer):
#     """
#         this is for register user we do no more thing,
#         first checked email or telegram_id has or doas not has,
#         second check email if it has and in side also check this email registered before or no,
#         if it registered we use raise ValidationError,
#         after we check password coming or no why we should check it because we writed required=False
#         because we register with email and password or with telegram_id so we should check password coming or no,
#         third we check telegram_id if it coming we make email with telegram_id ex telegram_id@telegram_id.com,
#         why we make email with telegram_id because our app required email field so we make email
#     """
#     re_password = serializers.CharField(write_only=True, required=False)
#     user_code = serializers.CharField(required=False)
#
#     class Meta:
#         models = CustomUser
#         fields = '__all__'
#
#     def validate(self, data):
#         email = data.get("email")
#         password = data.get("password")
#         re_password = data.get("re_password")
#         first_name = data.get("first_name", None)
#         google_id = data.get("google_id")
#
#         if not email and not google_id:
#             raise serializers.ValidationError("Email or Telegram ID is required.")
#
#         if email:
#             if CustomUser.objects.filter(email=email).exists():
#                 raise serializers.ValidationError("Email is already registered.")
#             if not password and not re_password:
#                 raise serializers.ValidationError("Password is required for email registration.")
#             if password != re_password:
#                 raise serializers.ValidationError({"password and re password": "there passwords not seme"})
#         if telegram_id:
#             email = f"{telegram_id}@telegram.com"
#             if CustomUser.objects.filter(email=email).exists():
#                 raise serializers.ValidationError("Telegram account is already registered.")
#
#         data["email"] = email
#         data["first_name"] = first_name
#         data["password"] = password
#         return data
#
#     def create(self, validated_data):
#         """
#             there we created one user and hashing password
#         """
#         password = validated_data.get("password", None)
#         user = CustomUser.objects.create(**validated_data)
#
#         if password:
#             user.password = make_password(password)
#
#         user.save()
#         return user
#
#
# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=False)
#     password = serializers.CharField(write_only=True, required=False)
#
#     def validate(self, data):
#         email = data.get("email")
#         password = data.get("password")
#         telegram_id = data.get("telegram_id")
#
#         if email and password:
#             user = CustomUser.objects.get(email=email)
#             if not user:
#                 raise serializers.ValidationError("Invalid email or password")
#         elif telegram_id:
#             try:
#                 user = CustomUser.objects.get(email=f"{telegram_id}@telegram.com")
#             except CustomUser.DoesNotExist:
#                 raise serializers.ValidationError("Telegram account not found")
#         else:
#             raise serializers.ValidationError("Email/Password or Telegram ID required")
#
#         if not user.is_active:
#             raise serializers.ValidationError("User is inactive")
#
#
#         data["user"] = user
#         return data


# class UserLogoutSerializer(serializers.Serializer):
#
#     def validate(self, attrs):
#         """
#          this is
#         """
#         request = self.context.get('request')
#         if request is None:
#             raise serializers.ValidationError({'error': 'Request object is missing from context.'})
#
#         if not hasattr(request, 'session'):
#             raise serializers.ValidationError({'error': 'Session object is not available in request.'})
#
#         refresh_token = request.session.get('refresh_token')
#         if not refresh_token:
#             raise serializers.ValidationError({'token': 'it is enable in session'})
#
#         self.token = refresh_token
#
#         return attrs
#
#
#
#     def save(self, **kwargs):
#
#         try:
#             RefreshToken(self.token).blacklist()
#         except TokenError:
#             self.fail('token failed')
#
#         request = self.context.get('request')
#
#         request.session.pop('refresh_token', None)
#
