from rest_framework import serializers
from django.shortcuts import get_object_or_404

from apps.quizzes.models import UserQuestion, Question


class SavedQuestionSerializer(serializers.ModelSerializer):
    question_id = serializers.UUIDField(write_only=True)
    class Meta:
        model = UserQuestion
        fields = ['question_id']

    def validate(self, data):
        user = self.context['request'].user

        if not  user and not user.is_authenticated:
            raise serializers.ValidationError({'detail':'Authentication credentials were not provided.'})

        question_id = data.get('question_id')
        if not question_id:
            raise serializers.ValidationError({'detail':'Question ID was not provided.'})

        question = get_object_or_404(Question, id=question_id)
        data['question'] = question
        data['user'] = user
        data['question_type'] = UserQuestion.QuestionType.Saved
        return data

