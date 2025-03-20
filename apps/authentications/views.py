from tokenize import TokenError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.urls import reverse
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from rest_framework.response import Response
from rest_framework import generics, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import CustomUser
from apps.authentications.service import get_user_from_refresh_token
from apps.authentications.serializers import ResetPasswordSerializer, RegisterSerializer, VerifyCodeSerializer, LoginSerializer, ForgetPasswordSerializer

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {"message": "Verif code send to your email"}
        return Response(data=data, status=status.HTTP_200_OK)


class VerifyCodeAndCreateUserAPIView(generics.GenericAPIView):
    serializer_class = VerifyCodeSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'User registered successfully'}
        return Response(data=data, status=status.HTTP_201_CREATED)


class LoginListAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    authentication_classes = ()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token is None:
            raise ValueError({'error': 'No refresh token provider'})
        token = RefreshToken(refresh_token)
        user_from_token = get_user_from_refresh_token(refresh_token)
        if request.user.id == user_from_token.id:
            raise ValueError({'error': 'This user not here'})
        try:
            token.blacklist()
        except TokenError:
            raise ValueError({'error': 'Token invalid or already used'})
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


class ForgetPasswordAPIView(generics.GenericAPIView):
    serializer_class = ForgetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.POST.get('email')
        user = CustomUser.objects.get(email=email)
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            # localhost:8000/reset-password/<encoded_pk>/<token>

            reset_url = reverse(
                "reset-password",
                kwargs={'encoded_pk':encoded_pk, 'token': token}
            )
            reset_url = f"localhost:8000{reset_url}"
            return Response({'message':f'Your password reset url: {reset_url}'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User does not exists'}, status=status.HTTP_400_BAD_REQUEST, )

class PasswordResetAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"kwargs": kwargs})
        serializer.is_valid(raise_exception=True)
        return Response({'message': "Password reset complete"}, status=status.HTTP_200_OK)

