from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from fcm_django.models import FCMDevice

class RegisterDeviceView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        device_id = request.data.get("device_id")
        user = request.user

        if not device_id:
            return Response({"error": "device_id is required"}, status=400)

        device, created = FCMDevice.objects.get_or_create(
            user=user,
            registration_id=device_id
        )

        if created:
            return Response({"message": "Device registered successfully."}, status=201)
        else:
            return Response({"message": "Device already registered."}, status=200)
