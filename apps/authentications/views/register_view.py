from rest_framework.response import Response
from rest_framework import generics, status
from apps.authentications.serializers.register_serializers import RegisterSerializer
from django.db import transaction
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    @transaction.atomic()
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {"message": "Verif code send to your email"}
        return Response(data=data, status=status.HTTP_200_OK)

