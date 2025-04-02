from rest_framework import generics

from apps.lessons.models import Chapter
from apps.lessons.serializers.chapter_serializer import ChapterSerializer


class ChapterListAPIView(generics.ListAPIView):
    """ This class is for Chapter List APIView!"""

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer