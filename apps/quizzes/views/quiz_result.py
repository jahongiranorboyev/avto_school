from rest_framework import generics
from apps.quizzes.serializers.quiz_result import UserQuestionCreateSerializer

class UserQuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = UserQuestionCreateSerializer
