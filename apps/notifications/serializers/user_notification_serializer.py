from rest_framework import serializers

from apps.notifications.models import UserNotification
from apps.notifications.serializers.custom_notification_serializer import CustomNotificationserializer
from apps.notifications.serializers.system_notification_serializer import SystemNotificationSerializer


class UserNotificationSerializer(serializers.ModelSerializer):
    custom_notification = CustomNotificationserializer(read_only=True)
    system_notification = SystemNotificationSerializer(read_only=True)
    class Meta:
        models = UserNotification
        fields = ['custom_notification', 'system_notification']
    