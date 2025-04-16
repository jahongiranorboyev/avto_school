<<<<<<< HEAD
from rest_framework import serializers

from apps.notifications.models import SystemNotification


class system_notification(serializers.ModelSerializer):
=======
from django.rest_fremwork import ModelSerializer


class system_notification(serializer.ModelSerializer):
>>>>>>> 2061695 (natofications and books apps changed)
    class Meta:
        models = SystemNotification
        fields = "__all__"

