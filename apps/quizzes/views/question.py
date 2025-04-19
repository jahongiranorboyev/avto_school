from rest_framework.generics import ListAPIView

from apps.quizzes.models import Question
from apps.quizzes.filters import QuestionFilter
from apps.quizzes.serializers import QuestionListSerializer

class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()
    filterset_class = QuestionFilter
