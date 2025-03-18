from django.db.models import Value
from django.core.cache import cache
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import CustomUser
from apps.authentications.email import email_service

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        full_name = attrs['full_name']
        email_service.send_massage(email)
        cache.set(f'reg_{email}', {
            "email": email,
            "password": password,
            "full_name": full_name
        }, timeout=2 * 60)
        return attrs


class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)
    coins = serializers.IntegerField(read_only=True)
    def validate(self, attrs):
        code = attrs['code']
        email = cache.get(f'user_email_{code}')
        saved_code = cache.get(f'user_code_{email}')

        user_data = cache.get(f'reg_{email}')
        if not saved_code or str(code) != str(saved_code):
            raise serializers.ValidationError({'error': 'The code is wrong or time is out'})

        if not user_data or not email:
            raise serializers.ValidationError({'data error': 'User data not found'})

        attrs['email'] = email
        return attrs


    def create(self, validated_data):
        email = validated_data['email']
        code = validated_data['code']
        coins = validated_data.get('coins', Value(0))

        # ======= get user values ============
        user_data = cache.get(f'reg_{email}')

        #===== deleted cache values ==========
        cache.delete(f'reg_{email}')
        cache.delete(f'code_{code}')

        # ============ create user used create_user method ================
        user = CustomUser.objects.create_user(
            email=user_data['email'],
            password=user_data['password'],
            full_name=user_data['full_name'],
        )
        return user



class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=50, required=True, write_only=True)
    email = serializers.EmailField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try:
            user = CustomUser.objects.get(email=email)
        except ValueError:
            raise serializers.ValidationError({'value error user': 'your password or email wrong'})

        if not user.check_password(password):
            raise serializers.ValidationError({'value error': 'your password or email wrong'})
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return {
            'access_token': str(access),
            'refresh_token': str(refresh),
            'email': user.email
        }


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True,write_only=True)

    class Meta:
        fields = ('email',)


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    def validate(self, attrs):
        password = attrs.get('password')
        token = self.context.get('kwargs').get('token')
        encoded_pk = self.context.get('kwargs').get('encoded_pk')

        if token is None or encoded_pk is None:
            raise serializers.ValidationError({'error': 'Missing data'})

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = CustomUser.objects.get(pk=pk)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError('The reset token invalid')

        user.set_password(password)
        user.save()
        return attrs




