<<<<<<< HEAD
from rest_framework import serializers

from apps.notifications.models import CustomNotification


class CustomNotificationserializer(serializers.ModelSerializer):
=======
from django.rest_fremwork import ModelSerializer


class CustomNotificationserializer(serializer.ModelSerializer):
>>>>>>> 2061695 (natofications and books apps changed)
    class Meta:
        models = CustomNotification
        fields = "__all__"