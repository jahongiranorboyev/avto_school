import django_filters
from apps.quizzes.models import UserQuestion, Question


class UserQuestionFilter(django_filters.FilterSet):
    is_my_correct_question = django_filters.BooleanFilter(method='filter_my_correct_question',label='Is my correct question')
    limit = django_filters.NumberFilter(method='filter_limit', label='question limit')
    mode = django_filters.ChoiceFilter(choices=Question.QuestionType.choices,method='filter_mode', label='mode')

    def filter_my_correct_question(self, queryset, name, value):
        user = self.request.user
        if value:
            return queryset.filter(user=user, question_type=UserQuestion.QuestionType.Correct)
        return queryset.filter(user=user)

    def filter_limit(self, queryset, name, value):
        return queryset[:value]

    def filter_mode(self, queryset, name, value):
        user = self.request.user
        if value :
            return queryset.filter(user=user, question__mode=value)
        return queryset.none()