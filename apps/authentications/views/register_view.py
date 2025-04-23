from django.db import transaction

from rest_framework import generics, status
from rest_framework.response import Response

from apps.authentications.email import email_service
from apps.authentications.serializers import RegisterSerializer
from django.utils.translation import gettext_lazy as _

class RegisterAPIView(generics.GenericAPIView):
    """
       API view for handling user registration.

       Uses RegisterSerializer to validate input data.
       Does not require authentication or permissions.
    """
    serializer_class = RegisterSerializer
    authentication_classes = ()
    permission_classes = ()

    @transaction.atomic()
    def post(self, request):
        """
            Handles POST request for user registration.

            Validates the incoming data using RegisterSerializer.
            If valid, sends a verification code to the user's email
            and returns a success message.

            The operation is wrapped in an atomic transaction to ensure data integrity.

            Returns:
                Response: HTTP 200 OK with a success message.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        email_service.send_massage(email=email, purpose='verify')

        data = {"message": _("Verif code send to your email")}
        return Response(data=data, status=status.HTTP_200_OK)