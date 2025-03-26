from rest_framework import generics

from apps.quizzes.models import QuestionCategory
from apps.quizzes.serializers.question import QuestionCategoryListSerializer


class QuestionCategoryListAPIView(generics.ListAPIView):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategoryListSerializer
