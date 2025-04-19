from rest_framework import serializers
from apps.quizzes.models import Question, QuestionVariant

class QuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVariant
        fields = ['id', 'title', 'is_correct']

class QuestionListSerializer(serializers.ModelSerializer):
    variants = QuestionVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'is_saved','description', 'mode', 'video', 'image', 'question_category', 'lesson', 'variants']
