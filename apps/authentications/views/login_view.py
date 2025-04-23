from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.authentications.serializers import LoginSerializer

class LoginAPIView(generics.GenericAPIView):
    """
        API view for handling user login.

        This view is used for user authentication. It accepts user credentials
        (email and password) and returns JWT tokens (access_token and refresh_token)
        if the authentication is successful.

        - Uses the LoginSerializer to validate user credentials (email and password).
        - If the credentials are valid, it returns the JWT tokens.
        - If the credentials are invalid, it raises a validation error with an appropriate message.
        - No authentication or permission is required to access this view, as it is for login purposes.
    """
    serializer_class = LoginSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        """
            Handle POST requests for user login.

            This method processes the request data (email and password), validates the
            credentials using the LoginSerializer, and returns JWT tokens if the login is successful.

            - If the authentication is successful, the response contains access_token and refresh_token.
            - If the authentication fails, a validation error is raised and a corresponding message is returned.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'access_token': serializer.validated_data['access_token'],
            'refresh_token': serializer.validated_data['refresh_token'],
        }, status=status.HTTP_200_OK)
