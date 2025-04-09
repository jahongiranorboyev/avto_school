from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.quizzes.models import UserQuestion
from apps.quizzes.serializers import UserQuestionSerializer
from apps.quizzes.filters import UserQuestionFilter

class UserQuestionView(generics.ListAPIView):
    serializer_class = UserQuestionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserQuestionFilter

    def get_queryset(self):
        return UserQuestion.objects.filter(user=self.request.user)

