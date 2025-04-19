from rest_framework import generics

from apps.quizzes.models import QuestionCategory, UserQuestionCategory
from apps.quizzes.serializers.question_category import QuestionCategoryListSerializer

class QuestionCategoryListAPIView(generics.ListAPIView):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategoryListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = self.request.user
        user_questions = UserQuestionCategory.objects.filter(user=user).values('question_category_id', 'last_quiz_results_avg')
        user_question_dict = {uq['question_category_id']: uq['last_quiz_results_avg'] for uq in user_questions}

        context['user_question_avg'] = user_question_dict
        return context