from rest_framework import status
from models import FCMDevice
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SendNotification(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        title = request.data.get('title')
        body = request.data.get('body')

        devices = FCMDevice.objects.filter(user=request.user)

        if not devices.exists():
            return Response({"error": "No devices found"}, status=status.HTTP_404_NOT_FOUND)
        
        all_messages = []
        for device in devices:
            match device.users.language:
                case 'eng':
                    title = ""
                case 'ru':
                    title = ""
                case 'uz':
                    title = ""
            message = messaging.Message(
                notification=messaging.Notification(title=title, body=body),token=device.id
            )

            response = messaging.send(message)
            all_messages.append({device.device_name: response})
        
        return Response("message": "Notifications sent")