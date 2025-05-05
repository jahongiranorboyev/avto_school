<<<<<<< HEAD
from rest_framework import serializers
from apps.notifications.models import SystemNotification


<<<<<<< HEAD
class system_notification(serializers.ModelSerializer):
=======
from django.rest_fremwork import ModelSerializer


class system_notification(serializer.ModelSerializer):
>>>>>>> 2061695 (natofications and books apps changed)
=======
class SystemNotificationSerializer(serializers.ModelSerializer):
>>>>>>> fe96ec7 (incomplement prosecc)
    class Meta:
        model = SystemNotification
        fields = '__all__'

    def validate(self, attrs):
        notification_type = attrs.get('notification_type')

        if notification_type == SystemNotification.NotificationType.LEVEL:
            if not attrs.get('level'):
                raise serializers.ValidationError("Level is required for notification type 'level'.")
        elif notification_type == SystemNotification.NotificationType.USER_CODE:
            if not attrs.get('friend_user'):
                raise serializers.ValidationError("friend_user is required for notification type 'user code'.")
        elif notification_type == SystemNotification.NotificationType.DISCOUNT:
            if not attrs.get('discount'):
                raise serializers.ValidationError("discount is required for notification type 'discount'.")
        elif notification_type == SystemNotification.NotificationType.ORDER:
            if not attrs.get('order'):
                raise serializers.ValidationError("order is required for notification type 'order'.")

        return attrs
