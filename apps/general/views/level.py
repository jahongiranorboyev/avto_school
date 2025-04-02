from rest_framework import generics

from apps.general.models.level import Level
from apps.general.serializers.level import LevelSerializer


class LevelCreateListAPIView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer