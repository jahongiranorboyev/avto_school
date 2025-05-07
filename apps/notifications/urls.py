from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.notifications.views import SystemNotificationViewSet
from apps.notifications.views.send_notification import SendNotificationToDeviceView
from apps.notifications.views.get_device_id import RegisterDeviceView

router = DefaultRouter()
router.register(r'system-notifications', SystemNotificationViewSet, basename='system-notification')

urlpatterns = [
    path('', include(router.urls)),
    path('send-to-device/', SendNotificationToDeviceView.as_view(), name='send_to_device'),
    path('register-device/', RegisterDeviceView.as_view(), name='register_device'),
]
