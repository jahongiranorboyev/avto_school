from django.db import models
from django.core.validators import MinValueValidator

from apps.utils.models import BaseModel



class General(BaseModel):
    user_code_discount = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )
    user_code_discount_is_percent = models.BooleanField(default=False)


    def __str__(self):
        return self.user_code_discount