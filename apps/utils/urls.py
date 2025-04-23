from django.urls import path
from apps.utils import views


urlpatterns = [
    path('language/', views.LanguageAPIView.as_view(), name='language-list'),
]

