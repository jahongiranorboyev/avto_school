from django.urls import path

from apps.quizzes.views import QuestionCategoryListAPIView

urlpatterns =[
    path('question-category-list/', QuestionCategoryListAPIView.as_view(), name='question-category-list'),
]