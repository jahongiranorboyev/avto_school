from rest_framework import serializers

from apps.notifications.models import CustomNotification


class CustomNotificationserializer(serializers.ModelSerializer):
    class Meta:
        models = CustomNotification
        fields = "__all__"