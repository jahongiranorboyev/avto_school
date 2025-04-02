from rest_framework import serializers

from apps.phrases.models import Phrase, UserCompletedPhrase


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = '__all__'

class UserPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompletedPhrase
        fields = '__all__'