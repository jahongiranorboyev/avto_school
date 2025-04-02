from rest_framework import generics

from apps.lessons.models import Lesson, LessonResource, LessonTerm, UserLesson
from apps.lessons.serializers import LessonSerializer, LessonResourceSerializer, LessonTermSerializer, \
    UserLessonSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonResourceListAPIView(generics.ListAPIView):
    queryset = LessonResource.objects.all()
    serializer_class = LessonResourceSerializer

class LessonTermsListAPIView(generics.ListAPIView):
    queryset = LessonTerm.objects.all()
    serializer_class = LessonTermSerializer


class UserLessonListAPIView(generics.ListAPIView):
    queryset = UserLesson.objects.all()
    serializer_class = UserLessonSerializer