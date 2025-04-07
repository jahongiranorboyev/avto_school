
from django.core.cache import cache
from rest_framework import serializers

from apps.users.models import CustomUser


class RegisterVerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)

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




class ForgetPasswordVerifyCodeSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)

    def validate(self, attrs):
        code = attrs['code']
        email = cache.get(f'user_email_{code}')
        print(email,'kkkkkkkkkkkkkkkkkkkk')

        saved_code = cache.get(f'user_code_{email}')
        print(saved_code, 'sssssssssssssssssssssssss')
        if not saved_code or str(code) != str(saved_code):
            raise serializers.ValidationError({'error': 'The code is wrong or time is out'})
        return attrs
