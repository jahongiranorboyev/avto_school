from rest_framework import serializers
from apps.quizzes.models import UserQuestion

class UserQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuestion
        fields = '__all__'


