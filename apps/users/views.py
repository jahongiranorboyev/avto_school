from rest_framework import generics

from apps.users.models import CustomUser
from apps.users.serializers import UserListSerializer, UserQuizzesDashboardSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = UserListSerializer


class UserQuizzesDashboardListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = UserQuizzesDashboardSerializer
