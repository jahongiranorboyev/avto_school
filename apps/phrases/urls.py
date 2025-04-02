from django.urls import path

from apps.phrases.views import PhraseListView, UserComplicatedPhraseListView

urlpatterns = [
    path('phrases/', PhraseListView.as_view(), name='phrase-list'),
    path('user-phrases/',UserComplicatedPhraseListView.as_view(), name='user-complicated-phrase-list'),
]