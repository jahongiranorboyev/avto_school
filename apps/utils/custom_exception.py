from rest_framework.exceptions import APIException
from rest_framework import status


class CustomAPIException(APIException):
    def __init__(self, message, status_code=status.HTTP_400_BAD_REQUEST):
        if isinstance(message, dict) and 'message' in message:
            self.detail = message
        else:
            self.detail = message

        self.status_code = status_code