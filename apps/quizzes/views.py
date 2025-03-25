from rest_framework import generics, permissions
from .models import (
    QuestionCategory, UserQuestionCategory, Question, QuestionVariant,
    SavedQuestion, CorrectQuestion, IncorrectQuestion,QuizResult
)
from .serializers import (
    QuestionCategorySerializer, UserQuestionCategorySerializer, QuestionSerializer,
<<<<<<< HEAD
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



=======
    QuestionVariantSerializer, SavedQuestionSerializer, CorrectQuestionSerializer,
    IncorrectQuestionSerializer, QuizeResultSerializer
)


# QuestionCategory API
class QuestionCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


# UserQuestionCategory API
class UserQuestionCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserQuestionCategory.objects.all()
    serializer_class = UserQuestionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class UserQuestionCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserQuestionCategory.objects.all()
    serializer_class = UserQuestionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


# Question API
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


# QuestionVariant API
class QuestionVariantListCreateAPIView(generics.ListCreateAPIView):
    queryset = QuestionVariant.objects.all()
    serializer_class = QuestionVariantSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionVariantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionVariant.objects.all()
    serializer_class = QuestionVariantSerializer
    permission_classes = [permissions.IsAuthenticated]


# SavedQuestion API
class SavedQuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = SavedQuestion.objects.all()
    serializer_class = SavedQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class SavedQuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedQuestion.objects.all()
    serializer_class = SavedQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


# CorrectQuestion API
class CorrectQuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = CorrectQuestion.objects.all()
    serializer_class = CorrectQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CorrectQuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CorrectQuestion.objects.all()
    serializer_class = CorrectQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


# IncorrectQuestion API
class IncorrectQuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = IncorrectQuestion.objects.all()
    serializer_class = IncorrectQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class IncorrectQuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IncorrectQuestion.objects.all()
    serializer_class = IncorrectQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


# QuizeResult API
class QuizeResultListCreateAPIView(generics.ListCreateAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizeResultSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuizeResultDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizeResultSerializer
    permission_classes = [permissions.IsAuthenticated]
>>>>>>> b6888bd (quizzes done !)
