from django.db import models
from django.core.validators import FileExtensionValidator

from apps.utils.models import BaseModel


class CustomNotification(BaseModel):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=10_000_00)
    image = models.FileField(
        upload_to='uploads/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )