
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from apps.users.models import Support
from apps.users.serializers import SupportSerializer


class SupportAPIView(generics.CreateAPIView):
    queryset = Support.objects.order_by('-created_at')
    serializer_class = SupportSerializer
    parser_classes = [MultiPartParser, FormParser]




