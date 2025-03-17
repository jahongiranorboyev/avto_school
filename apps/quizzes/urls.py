from django.urls import path
from .views import (
    QuestionCategoryListCreateAPIView, QuestionCategoryDetailAPIView,
    UserQuestionCategoryListCreateAPIView, UserQuestionCategoryDetailAPIView,
    QuestionListCreateAPIView, QuestionDetailAPIView,
    QuestionVariantListCreateAPIView, QuestionVariantDetailAPIView,
    SavedQuestionListCreateAPIView, SavedQuestionDetailAPIView,
    CorrectQuestionListCreateAPIView, CorrectQuestionDetailAPIView,
    IncorrectQuestionListCreateAPIView, IncorrectQuestionDetailAPIView,
    QuizeResultListCreateAPIView, QuizeResultDetailAPIView
)

urlpatterns = [
    path('categories/', QuestionCategoryListCreateAPIView.as_view(), name='question-category-list'),
    path('categories/<int:pk>/', QuestionCategoryDetailAPIView.as_view(), name='question-category-detail'),

    path('user-categories/', UserQuestionCategoryListCreateAPIView.as_view(), name='user-question-category-list'),
    path('user-categories/<int:pk>/', UserQuestionCategoryDetailAPIView.as_view(), name='user-question-category-detail'),

    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),

    path('question-variants/', QuestionVariantListCreateAPIView.as_view(), name='question-variant-list'),
    path('question-variants/<int:pk>/', QuestionVariantDetailAPIView.as_view(), name='question-variant-detail'),

    path('saved-questions/', SavedQuestionListCreateAPIView.as_view(), name='saved-question-list'),
    path('saved-questions/<int:pk>/', SavedQuestionDetailAPIView.as_view(), name='saved-question-detail'),

    path('correct-questions/', CorrectQuestionListCreateAPIView.as_view(), name='correct-question-list'),
    path('correct-questions/<int:pk>/', CorrectQuestionDetailAPIView.as_view(), name='correct-question-detail'),

    path('incorrect-questions/', IncorrectQuestionListCreateAPIView.as_view(), name='incorrect-question-list'),
    path('incorrect-questions/<int:pk>/', IncorrectQuestionDetailAPIView.as_view(), name='incorrect-question-detail'),

    path('quiz-results/', QuizeResultListCreateAPIView.as_view(), name='quiz-result-list'),
    path('quiz-results/<int:pk>/', QuizeResultDetailAPIView.as_view(), name='quiz-result-detail'),
]
