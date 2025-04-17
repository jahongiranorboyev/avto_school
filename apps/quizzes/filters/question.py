from django_filters import FilterSet , filters
from apps.quizzes.models import Question, QuestionCategory


class QuestionFilter(FilterSet):
    mode = filters.ChoiceFilter(choices=Question.QuestionType.choices)
    lesson = filters.UUIDFilter(field_name="lesson__id", lookup_expr="exact")
    question_category = filters.ModelMultipleChoiceFilter(
        queryset=QuestionCategory.objects.all(),
        field_name="question_category"
    )

    class Meta:
        model = Question
        fields = {
            "question_category": ["exact"],
        }


