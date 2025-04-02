from rest_framework import serializers

from apps.lessons.models import Lesson, LessonTerm, UserLesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTerm
        fields = '__all__'


class LessonResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLesson
        fields = '__all__'