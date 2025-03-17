from rest_framework import viewsets

from apps.roadsigns.models import RoadSign
from apps.roadsigns.serializers import RoadSignSerializer

class RoadSignViewSet(viewsets.ModelViewSet):
    queryset = RoadSign.objects.all()
    serializer_class = RoadSignSerializer
