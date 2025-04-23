from apps.authentications.serializers import ForgetPasswordSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from apps.authentications.email import email_service
from django.utils.translation import gettext_lazy as _
class ForgetPasswordAPIView(generics.GenericAPIView):
    """
       API view for handling the password reset request.

       - Uses the ForgetPasswordSerializer to validate the provided email.
       - Sends a verification code to the user's email for password reset if the email is valid.
       - Returns a response indicating whether the password reset code was successfully sent.

       Method:
           POST: Accepts email in the request body and sends a reset code to the provided email.
    """
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        """
            Handles the POST request for initiating the password reset process.

            Steps:
                - Validates the provided email using the ForgetPasswordSerializer.
                - If the email is valid, sends a verification code to the provided email.
                - Returns a response indicating the result of the operation.

            Returns:
                Response (200 OK): If the verification code is successfully sent to the email.
                Response (400/401): If the email is invalid or does not exist.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')

        # Send the password reset code to the user's email
        email_service.send_massage(email=email, purpose='reset')

        # Prepare a response message indicating the success of the operation
        data = _('We send your code to your email')

        return Response(data, status=status.HTTP_200_OK)
