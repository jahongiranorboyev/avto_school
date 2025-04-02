from django.urls import path

from apps.lessons.views.chapter_view import ChapterListAPIView
from apps.lessons.views.lesson_view import LessonListAPIView

urlpatterns = [
    path('chapters/', ChapterListAPIView.as_view(), name='chapter_list'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
]