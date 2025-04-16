from rest_framework import serializers
from apps.quizzes.models import UserQuestion, QuizResult


class UserQuestionCreateSerializer(serializers.Serializer):
    correct_answers = serializers.ListField(
        child=serializers.UUIDField(), required=False
    )
    incorrect_answers = serializers.ListField(
        child=serializers.UUIDField(), required=False
    )
    def validate(self, attrs):
        correct_answers = attrs.get('correct_answers', [])
        incorrect_answers = attrs.get('incorrect_answers', [])

        if not correct_answers or not incorrect_answers:
            raise serializers.ValidationError("At least 'correct_answers' or 'incorrect_answers' must be provided.")
        return attrs

    def create(self, validated_data):
        correct_answer_ids = validated_data.get("correct_answers", [])
        incorrect_answer_ids = validated_data.get("incorrect_answers", [])

        user = self.context["request"].user

        user_questions = []

        for correct_answer_id in correct_answer_ids:

            user_questions.append(UserQuestion(
                user_id=user.pk,
                question_id=correct_answer_id,
                question_type=UserQuestion.QuestionType.Correct
            ))

        for incorrect_answer_id in incorrect_answer_ids:
            user_questions.append(UserQuestion(
                user_id=user.pk,
                question_id=incorrect_answer_id,
                question_type=UserQuestion.QuestionType.Incorrect
            ))

        UserQuestion.objects.bulk_create(user_questions)
        QuizResult.objects.create(user=user, correct_answers=len(correct_answer_ids), incorrect_answers=len(incorrect_answer_ids))
        return validated_data
