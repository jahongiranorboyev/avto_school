from rest_framework import serializers

from apps.general.models.level import Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        read_only_fields = ('id','created_at','updated_at','created_by','updated_by')