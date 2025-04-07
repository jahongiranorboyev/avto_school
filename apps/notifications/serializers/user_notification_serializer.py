from django.rest_fremwork import ModelSerializer



class UserNotificationSerializer(serializer.ModelSerializer):
    custom_notification = CustomNotificationserializer(read_only=True)
    system_notification = system_notification(read_only=True)
    class Meta:
        models = UserNotification
        fields = ['custom_notification', 'system_notification']
    