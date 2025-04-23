from rest_framework.response import Response
from rest_framework import generics, status
from apps.authentications.serializers import ResetPasswordSerializer

from django.utils.translation import gettext_lazy as _

class ResetPasswordAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"kwargs": kwargs})
        serializer.is_valid(raise_exception=True)
        return Response({'message':_('hello world')}, status=status.HTTP_200_OK)

