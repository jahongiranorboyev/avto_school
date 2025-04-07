from rest_framework import generics

from apps.general.models.level import Level
from apps.general.serializers.level import LevelSerializer
from apps.general.views.custom_xception import CustomAPIException


class LevelCreateListAPIView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer