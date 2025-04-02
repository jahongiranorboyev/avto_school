from rest_framework.response import Response
from rest_framework import generics, status
from apps.authentications.serializers.login_serializer import LoginSerializer

class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    authentication_classes = ()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

