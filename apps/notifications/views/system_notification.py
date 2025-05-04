from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.notifications.models import SystemNotification
from apps.notifications.serializers import SystemNotificationSerializer


class SystemNotificationViewSet(ModelViewSet):
    queryset = SystemNotification.objects.all()
    serializer_class = SystemNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
