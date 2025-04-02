from rest_framework import generics

from apps.phrases.models import Phrase, UserCompletedPhrase
from apps.phrases.serializers import PhraseSerializer, UserPhraseSerializer


class PhraseListView(generics.ListCreateAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

class UserComplicatedPhraseListView(generics.ListCreateAPIView):
    queryset = UserCompletedPhrase.objects.all()
    serializer_class = UserPhraseSerializer
