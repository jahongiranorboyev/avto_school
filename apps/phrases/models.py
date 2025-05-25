from django.conf import settings
from django.db import models

from apps.utils.models import BaseModel


class Phrase(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class UserCompletedPhrase(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.id}'
