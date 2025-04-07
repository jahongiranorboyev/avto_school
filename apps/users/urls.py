from django.urls import path
from apps.users.views import UserListAPIView, EditProfileAPIView, SupportAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('edit-profile/', EditProfileAPIView.as_view(), name='edit-profile'),
    path('support/', SupportAPIView.as_view(), name='support-name')
]

