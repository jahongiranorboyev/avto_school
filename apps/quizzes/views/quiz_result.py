from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.quizzes.serializers.quiz_result import UserQuestionCreateSerializer

class UserQuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = UserQuestionCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User questions created successfully!"}, status=status.HTTP_201_CREATED)
