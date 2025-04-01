from django.shortcuts import render



class GetDeviceAPIView(APIView):
    def post():
        data = request.data
        device_id = data['device_id']
        if not device_id:
            return Response({"error": 'device id required'})
        Device.objects.create(device_id=device_id)
        return Response("success")

class UserAllNotification(APIView):
    authentication_class = (JWTAuthentication,)

    class get(self, request):
        user_id = request.user.id
        queryset = UserNotification.objects.filter(user_id=user_id, is_read=False)
        serializer = UserNotificationSerializer(queryset, many=True)
        return Response("result": {
            'notifications': serializer.data
        })

class system_notification(serializer):
    class Meta:
        models = SystemNotification
        fields = "__all__"

class CustomNotificationserializer(serializer):
    class Meta:
        models = CustomNotification
        fields = "__all__"

class UserNotificationSerializer(serializer):
    custom_notification = CustomNotificationserializer(read_only=True)
    system_notification = system_notification(read_only=True)
    class Meta:
        models = UserNotification
        fields = ['custom_notification', 'system_notification']
    