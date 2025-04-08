from rest_framework import generics

from apps.quizzes.filters.question import QuestionFilter
from apps.quizzes.models import Question
from apps.quizzes.pagination.question import CustomPagination
from apps.quizzes.serializers.question import QuestionListSerializer


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.prefetch_related('variants')
    serializer_class =  QuestionListSerializer
    pagination_class = CustomPagination
    filterset_class = QuestionFilter
