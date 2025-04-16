from django.db.models import Sum
from rest_framework import serializers

from apps.lessons.models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = '__all__'

    def get_duration(self, obj):
        return obj.chapter_lessons.aggregate(total=Sum('duration'))['total'] or 0