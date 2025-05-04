from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel


class SystemNotification(BaseModel):

    class NotificationType(models.TextChoices):
        LEVEL = 'level'
        USER_CODE = 'user code'
        DISCOUNT = 'discount'
        ORDER = 'order'


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_notifications')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='notifications/%Y/%m/%d', blank=True)
    notification_type = models.CharField(max_length=10, choices=NotificationType)
    level = models.ForeignKey('general.Level', on_delete=models.PROTECT)
    friend_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='friend_notifications')
    discount = models.ForeignKey('general.Discount', on_delete=models.PROTECT)
    order = models.ForeignKey('payments.Order', on_delete=models.PROTECT)

    def __str__(self):
        return self.title