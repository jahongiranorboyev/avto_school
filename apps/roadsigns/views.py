from rest_framework import generics

from apps.roadsigns.models import RoadSign
from apps.roadsigns.serializers import RoadSignSerializer


class RoadSignListAPIView(generics.ListAPIView):
    queryset = RoadSign.objects.all()
    serializer_class = RoadSignSerializer

