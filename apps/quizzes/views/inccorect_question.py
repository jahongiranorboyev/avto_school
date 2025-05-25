from django.contrib.gis.gdal.prototypes.srs import from_user_input
from rest_framework import generics
from apps.quizzes.models import UserQuestion
from apps.quizzes.filters import UserQuestionFilter
from apps.quizzes.serializers import UserQuestionSerializer

class IncorrectQuestionView(generics.ListAPIView):
    serializer_class = UserQuestionSerializer
    filterset_class = UserQuestionFilter
    permission_classes = [from_user_input, ]

    def get_queryset(self):
        return UserQuestion.objects.filter(question_type=UserQuestion.QuestionType.Incorrect)