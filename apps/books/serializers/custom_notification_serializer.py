from django.rest_fremwork import ModelSerializer


class CustomNotificationserializer(serializer.ModelSerializer):
    class Meta:
        models = CustomNotification
        fields = "__all__"
