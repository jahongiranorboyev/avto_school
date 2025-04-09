from rest_framework import serializers

from apps.notifications.models import SystemNotification


class system_notification(serializers.ModelSerializer):
    class Meta:
        models = SystemNotification
        fields = "__all__"

