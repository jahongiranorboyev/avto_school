from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework import generics

from apps.users.models import CustomUser, Support
from apps.users.serializers import UserListSerializer
from apps.quizzes.models.question import Question


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = UserListSerializer
    parser_classes = [MultiPartParser, FormParser]


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['total_questions'] = Question.objects.count()
        return context

