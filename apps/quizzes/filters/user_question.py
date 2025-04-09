import django_filters
from apps.quizzes.models import UserQuestion

class UserQuestionFilter(django_filters.FilterSet):
    question_type = django_filters.ChoiceFilter(choices=UserQuestion.QuestionType.choices)

    class Meta:
        model = UserQuestion
        fields = ['question_type']