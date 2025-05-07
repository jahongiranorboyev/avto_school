from django.urls import path
from apps.notifications.views.send_notification import SendNotificationToDeviceView
from apps.notifications.views.get_device_id import RegisterDeviceView

urlpatterns = [
    path('send-to-device/', SendNotificationToDeviceView.as_view(), name='send_to_device'),
    path('register-device/', RegisterDeviceView.as_view(), name='register_device'),
]
