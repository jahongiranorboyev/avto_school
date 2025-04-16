from rest_framework.generics import ListAPIView
from apps.quizzes.models import Question
from apps.quizzes.filters import QuestionFilter
from apps.quizzes.pagination.question import CustomPagination
from apps.quizzes.serializers import QuestionListSerializer
from django_filters.rest_framework import DjangoFilterBackend

class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionListSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuestionFilter

    def get_queryset(self):
        queryset = Question.objects.all()

        # Filtering applies here first
        queryset = self.filter_queryset(queryset)

        # Apply limit if exists
        limit = self.request.query_params.get('limit')
        if limit:
            try:
                limit = int(limit)
                queryset = queryset[:limit]
            except ValueError:
                pass  # Ignore if not valid int

        return queryset
