from rest_framework import generics, status
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

        obj, created = UserQuestion.objects.get_or_create(
            user=user, question_id=question.pk, question_type=question_type
        )

        if not created:
            obj.question.is_saved = False
            obj.question.save()
            obj.delete()
            return Response({'message': 'Saved question removed'}, status=status.HTTP_200_OK)

        question.is_saved = True
        question.save()
        return Response({'message': 'Saved question added'}, status=status.HTTP_201_CREATED)
