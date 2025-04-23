from django.db.models import Sum
from rest_framework import serializers

from apps.lessons.models import Chapter, UserChapter


class ChapterSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()
    completed_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = '__all__'

    def get_duration(self, obj):
        return obj.chapter_lessons.aggregate(total=Sum('duration'))['total'] or 0

    def get_completed_percentage(self, obj):
        user = self.context['request'].user
        if user.is_authenticated and obj.lessons > 0:
            user_chapter = UserChapter.objects.filter(user=user, chapter=obj).first()
            if user_chapter:
                percent = (user_chapter.completed_lessons / obj.lessons) * 100
                return round(percent, 2)
        return 0.0