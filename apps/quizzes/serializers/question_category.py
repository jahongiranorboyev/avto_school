from rest_framework import serializers

from apps.quizzes.models import QuestionCategory


class QuestionCategoryListSerializer(serializers.ModelSerializer):
    avg_result=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = QuestionCategory
        fields = '__all__'

    def get_avg_result(self, obj: QuestionCategory):
        user_question_dict = self.context.get('user_question_avg', {})
        return user_question_dict.get(obj.id, 0)



