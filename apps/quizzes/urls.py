from django.urls import path

from apps.quizzes.views import QuestionListAPIView
from apps.quizzes.views import IncorrectQuestionView
from apps.quizzes.views import UserQuestionCreateAPIView
from apps.quizzes.views import UserQuestionListAPIView
from apps.quizzes.views import QuestionCategoryListAPIView
from apps.quizzes.views import UserSavedQuestionCreateAPIView

urlpatterns =[
    path('question-list/', QuestionListAPIView.as_view(), name='question-list'),
    path('question-answer-create/', UserQuestionCreateAPIView.as_view(), name='question-answer-create'),
    path('question-category-list/', QuestionCategoryListAPIView.as_view(), name='question-category-list'),
    path('saved-question-create/', UserSavedQuestionCreateAPIView.as_view(), name='saved-question-create'),
    path('user-question-list/', UserQuestionListAPIView.as_view(), name='user-question-list'),
    path('incoorect-question-list/', IncorrectQuestionView.as_view(), name='user-question-list'),
]