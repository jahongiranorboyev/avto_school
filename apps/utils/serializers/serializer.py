from rest_framework import serializers

from apps.utils.models.language_m import CustomLanguage


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomLanguage
        fields = ('id', 'name', 'is_active', 'code',)