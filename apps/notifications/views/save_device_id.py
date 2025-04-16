<<<<<<< HEAD

=======
from django.shortcuts import render


class GetDeviceAPIView(APIView):
    def post():
        data = request.data
        device_id = data['device_id']
        if not device_id:
            return Response({"error": 'device id required'})
        Device.objects.create(device_id=device_id)
        return Response("success")
>>>>>>> 2061695 (natofications and books apps changed)
