from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.roadsigns.views import RoadSignViewSet

router = DefaultRouter()
router.register(r'roadsigns', RoadSignViewSet)

urlpatterns = [
    path('', include(router.urls)),
]