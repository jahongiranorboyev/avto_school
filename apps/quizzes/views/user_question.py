from rest_framework import generics
from apps.quizzes.models import UserQuestion
from apps.quizzes.filters import UserQuestionFilter
from apps.quizzes.serializers import UserQuestionSerializer

class UserQuestionListAPIView(generics.ListAPIView):
    serializer_class = UserQuestionSerializer
    filterset_class = UserQuestionFilter

    def get_queryset(self):
        return UserQuestion.objects.order_by('-created_at')

