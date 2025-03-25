from rest_framework import serializers

from apps.general.models import level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = level.Level
        fields = '__all__'
        read_only_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')