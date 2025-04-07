from django.db import models
from django.conf import settings

from apps.utils.models import BaseModel


class CustomNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='notifications/%Y/%m/%d', blank=True)
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title