from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel


class SystemNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_notifications')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='notifications/%Y/%m/%d', blank=True)
    notification_type = models.CharField(max_length=100)
    level = models.ForeignKey('general.Level', on_delete=models.PROTECT)
    friend_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='friend_notifications')
    discount = models.ForeignKey('general.Discount', on_delete=models.PROTECT)
    order = models.ForeignKey('payments.Order', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class CustomNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='notifications/%Y/%m/%d', blank=True)
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    system_notification = models.ForeignKey('notifications.SystemNotification', on_delete=models.PROTECT,related_name='sys_notifications')
    custom_notification = models.ForeignKey('notifications.CustomNotification', on_delete=models.PROTECT,related_name='custom_notifications')

    def __str__(self):
        return self.user.id
