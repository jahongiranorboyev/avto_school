import firebase_admin
from firebase_admin import credentials, messaging
from fcm_django.models import FCMDevice

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

class SendNotificationToDeviceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        device_id = request.data.get("device_id")

        if not device_id:
            return Response({"error": "device_id is required"}, status=400)

        try:
            device = FCMDevice.objects.select_related('user').get(id=device_id)
        except FCMDevice.DoesNotExist:
            return Response({"error": "Device not found"}, status=404)

        user = device.user
        lang = user.lang

        match lang:
            case 'eng':
                title = "Hello"
                body = "You have a new message"
            case 'ru':
                title = "Привет"
                body = "У вас есть новое сообщение"
            case 'uz':
                title = "Salom"
                body = "Sizda yangi xabar bor"
            case _:
                title = "Hello"
                body = "You have a new message"

        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=device.registration_id,
        )

        try:
            response = messaging.send(message)
            return Response({"message": f"Notification sent", "firebase_id": response}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)