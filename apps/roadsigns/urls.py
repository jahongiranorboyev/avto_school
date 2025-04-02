from django.urls import path

from apps.roadsigns.views import RoadSignListAPIView


urlpatterns = [
   path('roadsigns/', RoadSignListAPIView.as_view(),name='roadsign-list'),
]