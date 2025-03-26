import uuid
from django.db import models
from django.conf import settings

class BaseModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="+",
        editable=False,
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        on_delete=models.SET_NULL,
        related_name="+",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.pk is None:
            self.id = str(uuid.uuid4())
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
