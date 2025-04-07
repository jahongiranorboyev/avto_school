from django.urls import path
from apps.authentications.views.login_view import LoginAPIView
from apps.authentications.views.register_view import RegisterAPIView
from apps.authentications.views.reset_password_view import ResetPasswordAPIView
from apps.authentications.views.forget_password_view import ForgetPasswordAPIView
from apps.authentications.views.verify_code_view import ForgetPasswordVerifyCodeAPIView, RegisterVerifyCodeSerializer, \
    RegisterVerifyCodeAPIView
from apps.authentications.views.base_views import GoogleAuthAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login-user'),
    path('register/', RegisterAPIView.as_view(), name='register-user'),
    path('register-verify-code/', RegisterVerifyCodeAPIView.as_view(), name='register-verify-code'),
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='forget-password'),
    path('forget-password-verify-code/',
         ForgetPasswordVerifyCodeAPIView.as_view(),
         name='forget-password-verify-code'),
    path('reset-password/<str:encoded_pk>/<str:token>',
         ResetPasswordAPIView.as_view(),
         name='reset-password'),
    path('google/', GoogleAuthAPIView.as_view(), name='validate_auth_token'),
]
