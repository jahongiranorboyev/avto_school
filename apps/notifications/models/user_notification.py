from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel


class UserNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    system_notification = models.ForeignKey('notifications.SystemNotification', on_delete=models.PROTECT,related_name='sys_notifications')
    custom_notification = models.ForeignKey('notifications.CustomNotification', on_delete=models.PROTECT,related_name='custom_notifications')
<<<<<<< HEAD
    is_read = models.BooleanField(default=False)
=======
    is_read = models.BoolenField(default=False)
>>>>>>> 2061695 (natofications and books apps changed)
    
    def __str__(self):
        return self.user.id
