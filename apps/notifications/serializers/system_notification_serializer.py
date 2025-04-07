from django.rest_fremwork import ModelSerializer


class system_notification(serializer.ModelSerializer):
    class Meta:
        models = SystemNotification
        fields = "__all__"

