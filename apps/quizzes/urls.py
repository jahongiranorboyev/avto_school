from django.urls import path
from .views import (
    QuestionCategoryListCreateAPIView, QuestionCategoryDetailAPIView,
    UserQuestionCategoryListAPIView, UserQuestionCategoryDetailAPIView,
    QuestionListCreateAPIView, QuestionDetailAPIView,
    SavedQuestionListCreateAPIView, SavedQuestionDetailAPIView,
    QuizResultCreateView
)

urlpatterns = [
    path('categories/', QuestionCategoryListCreateAPIView.as_view(), name='question-category-list'),
    path('categories/<int:pk>/', QuestionCategoryDetailAPIView.as_view(), name='question-category-detail'),

    path('user-categories/', UserQuestionCategoryListAPIView.as_view(), name='user-question-category-list'),
    path('user-categories/<int:pk>/', UserQuestionCategoryDetailAPIView.as_view(), name='user-question-category-detail'),

    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('saved-questions/', SavedQuestionListCreateAPIView.as_view(), name='saved-question-list'),
    path('saved-questions/<int:pk>/', SavedQuestionDetailAPIView.as_view(), name='saved-question-detail'),
    path('quiz-results/', QuizResultCreateView.as_view(), name='quiz-result-list'),
]
