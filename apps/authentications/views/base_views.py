from rest_framework import generics, status
from rest_framework.response import Response

from apps.authentications.serializers import GoogleSocialAuthSerializer


class GoogleAuthAPIView(generics.GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_200_OK)