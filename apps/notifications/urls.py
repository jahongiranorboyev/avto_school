from django.urls import path
from apps.notifications.views.send_notification import SendNotificationToDeviceView

urlpatterns = [
    path('send-to-device/', SendNotificationToDeviceView.as_view(), name='send_to_device'),
]
