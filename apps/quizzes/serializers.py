from rest_framework import serializers
<<<<<<< HEAD
from django.contrib.auth import get_user_model
=======
>>>>>>> b6888bd (quizzes done !)
from .models import (
    QuestionCategory, UserQuestionCategory, Question, QuestionVariant,
    SavedQuestion, CorrectQuestion, IncorrectQuestion, QuizResult
)
<<<<<<< HEAD
from ..lessons.models import Lesson

User = get_user_model()
=======
>>>>>>> b6888bd (quizzes done !)


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

<<<<<<< HEAD
=======

class QuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVariant
        fields = '__all__'


>>>>>>> b6888bd (quizzes done !)
class SavedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedQuestion
        fields = '__all__'

<<<<<<< HEAD
class QuizResultSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    quiz_category_id = serializers.IntegerField(write_only=True, required=False)
    lesson_id = serializers.IntegerField(write_only=True, required=False)
    total_questions = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = QuizResult
        fields = (
            "id", "user_id", "quiz_category_id",
            "lesson_id", "total_questions",
            "correct_answers", "incorrect_answers"
        )

    def create(self, validated_data):
        user_id = validated_data.get("user_id")
        quiz_category_id = validated_data.get("quiz_category_id")
        lesson_id = validated_data.get("lesson_id")
        total_questions = validated_data.get("total_questions", [])

        try:
            user = User.objects.get(id=user_id)
            category = QuestionCategory.objects.get(id=quiz_category_id) if quiz_category_id else None
            lesson = Lesson.objects.get(id=lesson_id) if lesson_id else None
        except (User.DoesNotExist, QuestionCategory.DoesNotExist, Lesson.DoesNotExist):
            raise serializers.ValidationError({"error": "Invalid user, category, or lesson"})

        correct_count = 0
        incorrect_count = 0

        for q in total_questions:
            question_id = q.get("question_id")
            selected_variant_id = q.get("selected_variant_id")

            try:
                selected_variant = QuestionVariant.objects.get(id=selected_variant_id, question_id=question_id)
                if selected_variant.is_correct:
                    CorrectQuestion.objects.create(user=user, question_id=question_id)
                    correct_count += 1
                    user.coins += 1
                    user.save()
                else:
                    IncorrectQuestion.objects.create(user=user, question_id=question_id)
                    incorrect_count += 1
            except QuestionVariant.DoesNotExist:
                continue

        total = correct_count + incorrect_count

        quiz_result = QuizResult.objects.create(
            user=user,
            correct_answers=correct_count,
            incorrect_answers=incorrect_count,
            total_questions=total,
            lesson=lesson
        )
        if category:
            quiz_result.question_category.add(category)

        return quiz_result
=======

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
>>>>>>> b6888bd (quizzes done !)
