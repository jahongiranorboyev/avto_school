from rest_framework import generics
from rest_framework.response import Response

from apps.quizzes.models import UserQuestion
from apps.quizzes.serializers.saved_question import SavedQuestionSerializer


class UserSavedQuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = SavedQuestionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        question = serializer.validated_data['question']
        question_type = serializer.validated_data['question_type']

        saved_question = UserQuestion.objects.filter(
            user=user, question=question, question_type=question_type
        ).first()

        if saved_question:
            saved_question.delete()
            return Response({'message': 'Saved question removed'}, status=200)

        UserQuestion.objects.create(user=user, question=question, question_type=question_type)
        return Response({'message': 'Saved question added'}, status=201)


