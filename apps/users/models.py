from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import UserManager, AbstractUser

from apps.utils.models.base_model import BaseModel



class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email=None, password=None, full_name=None, **extra_fields):
        extra_fields["full_name"] = full_name
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, full_name=None, **extra_fields):
        extra_fields['is_staff'] = extra_fields['is_superuser'] = True
        extra_fields["full_name"] = full_name
        return self._create_user(email, password, **extra_fields)


class CustomUser(BaseModel, AbstractUser):
    class AuthProviders(models.TextChoices):
        EMAIL = 'email', "Email"
        GOOGLE = 'google', "Google"
        TELEGRAM = 'telegram', "telegram"
        INSTAGRAM = 'instagram', "instagram"

    username = None
    email = models.EmailField(unique=True)
    icon = models.ImageField(upload_to='users/icons/',
                             blank=True,
                             null=True,
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['jpg', 'jpeg', 'png'])],
                             )

    objects = CustomUserManager()
    full_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    user_code = models.CharField(max_length=50, unique=True,blank=True,null=True)
    balance = models.PositiveSmallIntegerField(default=0)
    coins = models.PositiveSmallIntegerField(default=0)
    correct_answers = models.FloatField(default=0)
    last_10_quiz_results_avg = models.FloatField(default=0)
    order_expire_date = models.DateTimeField(auto_now_add=True)
    auth_provider = models.CharField(
        max_length=50,
        default=AuthProviders.EMAIL)

