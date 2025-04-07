
from apps.authentications.serializers.forget_password_serializer import ForgetPasswordSerializer
from apps.authentications.email import email_service
from rest_framework import generics, status
from rest_framework.response import Response

class ForgetPasswordAPIView(generics.GenericAPIView):
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        email_service.send_massage(email)
        data = 'We send your code to your email'
        return Response(data, status=status.HTTP_200_OK)

