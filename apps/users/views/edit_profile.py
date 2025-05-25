from django.utils.translation import gettext_lazy as _

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from apps.users.models import CustomUser
from apps.users.serializers import EditProfileSerializer
from apps.utils.custom_exception import CustomAPIException


class EditProfileAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = EditProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.id != self.request.user.id:
            raise CustomAPIException(message=_("this user not you"))
        return obj

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

