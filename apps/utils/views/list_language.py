from rest_framework import generics

from apps.utils.models import CustomLanguage
from apps.utils.serializers.serializer import LanguageSerializer


class LanguageAPIView(generics.ListAPIView):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        return CustomLanguage.languages()

