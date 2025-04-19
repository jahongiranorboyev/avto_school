from django_filters import FilterSet , filters
from apps.quizzes.models import Question, QuestionCategory


class QuestionFilter(FilterSet):
    mode = filters.ChoiceFilter(choices=Question.QuestionType.choices)
    limit = filters.NumberFilter(label='limit', method='filter_limit')
    lesson = filters.UUIDFilter(field_name="lesson__id", lookup_expr="exact")
    question_category = filters.ModelMultipleChoiceFilter(
        queryset=QuestionCategory.objects.all(),
        field_name="question_category"
    )
    def filter_limit(self, queryset, name, value):
        if value is None:
            return queryset
        return queryset[:value]

    class Meta:
        model = Question
        fields = {
            "question_category": ["exact"],
        }


