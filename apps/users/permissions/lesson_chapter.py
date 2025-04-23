from apps.lessons.models import Chapter

from .base_paid_content_permission import BasePaidContentPermission


class CanAccessChapter(BasePaidContentPermission):
    model = Chapter