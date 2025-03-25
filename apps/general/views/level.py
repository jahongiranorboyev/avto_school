from rest_framework import generics

from apps.general.models import Level
from apps.general.serializers.level import LevelSerializer


class LevelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
