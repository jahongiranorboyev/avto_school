
from django.contrib.auth.models import  AbstractUser

from apps.utils.models.base_model import BaseModel

class CustomUser(BaseModel, AbstractUser):
    pass
