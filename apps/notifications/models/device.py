from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=255, unique=True)
    fcm_token = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

