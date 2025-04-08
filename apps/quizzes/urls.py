from django.urls import path

from apps.quizzes.views.quiz_result import UserQuestionCreateAPIView
from apps.quizzes.views.question_category import QuestionCategoryListAPIView
from apps.quizzes.views.saved_question import UserSavedQuestionCreateAPIView
from apps.quizzes.views.question import QuestionListAPIView
from apps.quizzes.views.user_question import UserQuestionView

urlpatterns =[
    path('question-list/', QuestionListAPIView.as_view(), name='question-list'),
    path('question-answer-create/', UserQuestionCreateAPIView.as_view(), name='question-answer-create'),
    path('question-category-list/', QuestionCategoryListAPIView.as_view(), name='question-category-list'),
    path('saved-question-create/', UserSavedQuestionCreateAPIView.as_view(), name='saved-question-create'),
    path('user-question-list/', UserQuestionView.as_view(), name='user-question-list'),
]