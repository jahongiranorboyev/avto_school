from rest_framework import serializers
from .models import (
    QuestionCategory, UserQuestionCategory, Question, QuestionVariant,
    SavedQuestion, CorrectQuestion, IncorrectQuestion, QuizResult
)


class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = '__all__'


class UserQuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuestionCategory
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVariant
        fields = '__all__'


class SavedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedQuestion
        fields = '__all__'


class CorrectQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectQuestion
        fields = '__all__'


class IncorrectQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncorrectQuestion
        fields = '__all__'


class QuizeResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = '__all__'
