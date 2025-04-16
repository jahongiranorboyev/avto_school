from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

User = get_user_model()

class ForceUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.user = User.objects.first()
        except User.DoesNotExist:
            request.user = AnonymousUser()

        response = self.get_response(request)
        return response