from django.urls import path
from apps.authentications.views import PasswordResetAPIView, RegisterAPIView, VerifyCodeAndCreateUserAPIView, LoginListAPIView, LogoutView, ForgetPasswordAPIView
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('verify/', VerifyCodeAndCreateUserAPIView.as_view(), name="verify"),
    path('login/', LoginListAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password/',ForgetPasswordAPIView.as_view(),name='reset-password',),
    path('reset-password/<str:encoded_pk>/<str:token>',PasswordResetAPIView.as_view(),name='reset-password',),
]