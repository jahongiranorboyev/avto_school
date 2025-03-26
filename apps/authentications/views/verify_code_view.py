from django.utils import cache
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from rest_framework.response import Response
from rest_framework import generics, status

from apps.authentications.serializers.verify_code_serializers import (
    RegisterVerifyCodeSerializer, ForgetPasswordVerifyCodeSerializer)
from apps.users.models import CustomUser


class RegisterVerifyCodeAPIView(generics.GenericAPIView):
    serializer_class = RegisterVerifyCodeSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'User registered successfully'}
        return Response(data=data, status=status.HTTP_201_CREATED)




class ForgetPasswordVerifyCodeAPIView(generics.GenericAPIView):
    serializer_class = ForgetPasswordVerifyCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        email = cache.get(f'user_email_{code}')
        user = CustomUser.objects.get(email=email)
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            # localhost:8000/reset-password/<encoded_pk>/<token>

            reset_url = reverse(
                "reset-password",
                kwargs={'encoded_pk': encoded_pk, 'token': token}
            )

            reset_url = f"localhost:8000{reset_url}"
            return Response({'message': f'Your password reset url: {reset_url}'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User does not exists'}, status=status.HTTP_400_BAD_REQUEST, )

