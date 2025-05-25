from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel


class UserNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    system_notification = models.ForeignKey('notifications.SystemNotification', on_delete=models.PROTECT,related_name='sys_notifications')
    custom_notification = models.ForeignKey('notifications.CustomNotification', on_delete=models.PROTECT,related_name='custom_notifications')

    is_read = models.BooleanField(default=False)

    
    def __str__(self):
        return f'{self.user.id}'
