from apps.general.serializer import TariffSerializer
from apps.general.models import Tariff
from rest_framework import generics


class TariffListCreateAPIView(generics.ListAPIView):
    queryset = Tariff.objects.order_by('-created_at')
    serializer_class = TariffSerializer