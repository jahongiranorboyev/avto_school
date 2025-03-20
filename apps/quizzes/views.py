from rest_framework import generics, permissions
from .models import (
    QuestionCategory, UserQuestionCategory, Question, QuestionVariant,
    SavedQuestion, CorrectQuestion, IncorrectQuestion,QuizResult
)
from .serializers import (
    QuestionCategorySerializer, UserQuestionCategorySerializer, QuestionSerializer,
     SavedQuestionSerializer, QuizResultSerializer
)


# QuestionCategory API
class QuestionCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer


class QuestionCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer


# UserQuestionCategory API
class UserQuestionCategoryListAPIView(generics.ListAPIView):
    queryset = UserQuestionCategory.objects.all()
    serializer_class = UserQuestionCategorySerializer


class UserQuestionCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserQuestionCategory.objects.all()
    serializer_class = UserQuestionCategorySerializer


# Question API
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# SavedQuestion API
class SavedQuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = SavedQuestion.objects.all()
    serializer_class = SavedQuestionSerializer

class SavedQuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedQuestion.objects.all()
    serializer_class = SavedQuestionSerializer


class QuizResultCreateView(generics.CreateAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer



