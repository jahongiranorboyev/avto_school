from django.urls import path
from apps.users.views import UserListAPIView, UserQuizzesDashboardListAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('user-quizzes-dashboard/', UserQuizzesDashboardListAPIView.as_view(), name='user-quizzes-dashboard'),
]

