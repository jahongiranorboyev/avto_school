from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.utils.custom_exception import CustomAPIException
from apps.quizzes.models import UserQuestion, QuizResult, Question


class UserQuestionCreateSerializer(serializers.Serializer):
    correct_answers = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True,
        required=False
    )
    incorrect_answers = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True,
        required=False
    )

    @classmethod
    def check_valid_questions(cls, correct_answers_ids=None, incorrect_answers_ids=None) -> None:
        """ check valid questions """
        correct_answers_ids = correct_answers_ids or []
        incorrect_answers_ids = incorrect_answers_ids or []

        if set(correct_answers_ids).issubset(set(incorrect_answers_ids)) or set(incorrect_answers_ids).issubset(set(correct_answers_ids)):
            raise CustomAPIException(_('Same question answers were provided in both lists.'))

        CACHE_KEY = 'all_questions'
        all_questions = cache.get(CACHE_KEY)
        if all_questions is None:
            all_questions = list(Question.objects.values_list('id', flat=True))
            cache.set(CACHE_KEY, all_questions, timeout=60 * 60)

        submitted_ids = set(correct_answers_ids + incorrect_answers_ids)
        valid_ids = set(all_questions)

        if not submitted_ids.issubset(valid_ids):
            raise CustomAPIException({
                'question': _('A question_id was not found in questions!')
            })

    def validate(self, attrs):
        correct_answers_ids = attrs.get('correct_answers', [])
        incorrect_answers_ids = attrs.get('incorrect_answers', [])

        if correct_answers_ids is None or incorrect_answers_ids is None:
            raise CustomAPIException(_("At least 'correct_answers' or 'incorrect_answers' must be provided."))

        self.check_valid_questions(correct_answers_ids, incorrect_answers_ids)

        return attrs

    def create(self, validated_data):
        correct_answer_ids = validated_data.get("correct_answers", [])
        incorrect_answer_ids = validated_data.get("incorrect_answers", [])
        user = self.context["request"].user

        UserQuestion.objects.filter(
            user=user,
            question_id__in=correct_answer_ids + incorrect_answer_ids
        ).delete()

        user_questions = []

        for correct_id in correct_answer_ids:
            user_questions.append(UserQuestion(
                question_id=correct_id,
                user=user,
                question_type=UserQuestion.QuestionType.Correct
            ))

        for incorrect_id in incorrect_answer_ids:
            user_questions.append(UserQuestion(
                question_id=incorrect_id,
                user=user,
                question_type=UserQuestion.QuestionType.Incorrect
            ))

        UserQuestion.objects.bulk_create(user_questions)
        QuizResult.objects.create(
            user=user,
            correct_answers=len(correct_answer_ids),
            incorrect_answers=len(incorrect_answer_ids)
        )

        return validated_data



