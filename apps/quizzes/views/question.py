from rest_framework.generics import ListAPIView
from apps.quizzes.models import Question
from apps.quizzes.filters import QuestionFilter
from apps.quizzes.pagination.question import CustomPagination
from apps.quizzes.serializers import QuestionListSerializer
from django_filters.rest_framework import DjangoFilterBackend

class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()
    pagination_class = CustomPagination
    filterset_class = QuestionFilter
