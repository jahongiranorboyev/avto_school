from django.urls import path

from apps.authentications.views import (
    LogoutView,
    LoginAPIView,
    RegisterAPIView,
    GoogleAuthAPIView,
    ResetPasswordAPIView,
    ForgetPasswordAPIView,
    RegisterVerifyCodeAPIView,
    ForgetPasswordVerifyCodeAPIView,
)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login-user'),
    path('logout/', LogoutView.as_view(), name='logout-user'),
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
