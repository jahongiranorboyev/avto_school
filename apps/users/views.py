from rest_framework import generics

from apps.users.models import CustomUser
from apps.users.serializers import UserListSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.order_by('-pk')
    serializer_class = UserListSerializer