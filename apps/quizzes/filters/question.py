import django_filters
from apps.quizzes.models import Question, QuestionCategory


class QuestionFilter(django_filters.FilterSet):
    mode = django_filters.ChoiceFilter(choices=Question.QuestionType.choices)
    limit = django_filters.NumberFilter(method="filter_limit",label="Limit the number of questions")
    lesson = django_filters.NumberFilter(field_name="lesson__id", lookup_expr="exact")
    # is_my_incorrect_questions = django_filters.BooleanFilter(method="filter_is_my_incorrect_questionses")
    question_category = django_filters.ModelMultipleChoiceFilter(
        queryset=QuestionCategory.objects.all() ,
        field_name="question_category",
        label="Filter by category"
    )


    def filter_limit(self, queryset, name, value):
        if value:
            return queryset[:value]
        return queryset

    class Meta:
        model = Question
        fields = ["mode", "limit","question_category", "lesson"]
