from rest_framework import generics
from apps.users.models import CustomUser
from apps.users.serializers import PromoCodeSerializer
from apps.utils.custom_exception import CustomAPIException
from django.utils.translation import gettext_lazy as _

class PromoCodeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = PromoCodeSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.id != self.request.user.id:
            raise CustomAPIException(message=_('Can not get any info about this user'))
        return obj