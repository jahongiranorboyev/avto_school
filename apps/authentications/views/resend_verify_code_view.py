from rest_framework import views, generics
from rest_framework.response import Response

from django.utils.translation import gettext_lazy as _
from apps.authentications.email import email_service
from apps.authentications.serializers import ReSendVerifyCodeSerializer


class ReSendVerifyCodeAPIView(generics.CreateAPIView):
    serializer_class = ReSendVerifyCodeSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        saved_code = serializer.validated_data.get('saved_code')
        email_service.send_massage(email=email, purpose='reset', code=saved_code)
        return Response(_('We send again your code please check your email'))
