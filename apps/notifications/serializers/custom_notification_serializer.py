from rest_framework import serializers

from apps.notifications.models import CustomNotification


class CustomNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        models = CustomNotification
        fields = "__all__"