from rest_framework import serializers

from apps.quizzes.models import QuestionCategory, UserQuestionCategory


class QuestionCategoryListSerializer(serializers.ModelSerializer):
    avg_result=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = QuestionCategory
        fields = '__all__'

    def get_avg_result(self,obj: QuestionCategory):
        # user = self.context['request'].user
        # user_question, _ = UserQuestionCategory.objects.get(user=user, question_category_id=obj.id)
        return 65



