from rest_framework.response import Response
from rest_framework import generics, status

from apps.authentications.serializers import (
    RegisterVerifyCodeSerializer, ForgetPasswordVerifyCodeSerializer)
from django.utils.translation import gettext_lazy as _

class RegisterVerifyCodeAPIView(generics.GenericAPIView):
    """
        API view for verifying the registration code and creating a new user.

        This endpoint:
        - Accepts the verification code and email from the client.
        - Validates the code against cached data.
        - If valid, creates a new user using the cached registration data.
        - Returns a success response upon successful registration.
    """
    serializer_class = RegisterVerifyCodeSerializer
    permission_classes = ()
    authentication_classes = ()
    def post(self, request):
        # ===== Deserialize and validate the input data =====
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # ===== Return a success response =====
        data = {'message': _('User registered successfully')}

        return Response(data=data, status=status.HTTP_201_CREATED)


class ForgetPasswordVerifyCodeAPIView(generics.GenericAPIView):
    """
        API view for verifying the code sent to the user's email during the password reset process.

        - Uses the ForgetPasswordVerifyCodeSerializer to validate the provided email and verification code.
        - If the code is valid and the user exists, returns success response.
        - If validation fails (e.g., wrong code or email), returns appropriate error response from serializer.

        Method:
            POST: Accepts email and code in the request body.
    """
    serializer_class = ForgetPasswordVerifyCodeSerializer

    def post(self, request):
        # ===== Serialize and validate incoming data (code + email) =====
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # ===== If validation passed, return success message =====
        return Response({'message': _('You can change your password')}, status=status.HTTP_200_OK)