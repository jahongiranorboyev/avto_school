from rest_framework import generics

from apps.users.models import Support
from apps.users.serializers import SupportSerializer


class SupportAPIView(generics.CreateAPIView):
    queryset = Support.objects.all().order_by('-created_at')
    serializer_class = SupportSerializer





