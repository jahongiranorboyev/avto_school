from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from apps.quizzes.models import UserQuestion, Question
from apps.utils.custom_exception import CustomAPIException


class SavedQuestionSerializer(serializers.ModelSerializer):
    question_id = serializers.UUIDField(write_only=True)
    class Meta:
        model = UserQuestion
        fields = ['question_id']

    def validate(self, data):
        user = self.context['request'].user

        if not  user and not user.is_authenticated:
            raise CustomAPIException({'detail':_('Authentication credentials were not provided.')})

        question_id = data.get('question_id')
        if not question_id:
            raise CustomAPIException({'detail':_('Question ID was not provided.')})

        question = Question.objects.get(id=question_id)
        if question is None:
            raise CustomAPIException({'detail':_('Question ID was not provided.')})

        data['question'] = question
        data['user'] = user
        data['question_type'] = UserQuestion.QuestionType.Saved
        return data

