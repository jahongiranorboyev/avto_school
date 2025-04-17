from apps.quizzes.models import QuestionCategory
from .base_paid_content_permission import BasePaidContentPermission

class CanAccessQuestion(BasePaidContentPermission):
    model = QuestionCategory
