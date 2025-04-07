from django.db.models import Sum
from rest_framework import serializers

from apps.lessons.models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

    def validate_duration(self, value):
        lessons = value.lessons_set.all()
        if not lessons.exists():
            return 0
        total_duration = lessons.aggregate(total=Sum('duration'))
        return total_duration or 0
