from rest_framework import generics

from apps.general.models.tariff import Tariff
from apps.general.serializers.tariff import TariffSerializer


class TariffListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer