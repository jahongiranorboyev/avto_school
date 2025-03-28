import random
import string

from django.db import models
from django.db.models import Sum, Avg
from django.contrib.auth.hashers import make_password
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import UserManager, AbstractUser

from apps.general.models import Level
from apps.quizzes.models import QuizResult
from apps.utils.models.base_model import BaseModel
from rest_framework_simplejwt.tokens import RefreshToken



class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
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

    level = models.ForeignKey('general.Level', on_delete=models.CASCADE, blank=True, null=True)
    user_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    balance = models.PositiveSmallIntegerField(default=0)
    coins = models.PositiveSmallIntegerField(default=0)
    correct_answers = models.FloatField(default=0)
    last_10_quiz_results_avg = models.FloatField(default=0)
    order_expire_date = models.DateTimeField(auto_now_add=True)
    auth_provider = models.CharField(
        max_length=50,
        default=AuthProviders.EMAIL)


    def __str__(self):
        return f'Full name: {self.full_name}'


    def clean(self):
        super().clean()
        len_full_name = len(self.full_name.strip().split())
        if len_full_name != 2:
            raise ValueError({'error': 'Full name should be like this Jon Dou'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.pk:
            self.update_level()


    def update_level(self):
        if self.level is not None:
            """
                Foydalanuvchi coins asosida darajasini yangilaydi.
            """

            min_level = Level.objects.all().order_by('coins').first()
            max_level = Level.objects.all().order_by('coins').last()
            if min_level and max_level is not None:
                if self.coins < max_level.coins:
                    if self.coins >= min_level.coins:
                        users_level_coins = Level.objects.all().order_by('-coins')
                        for index, level_data in enumerate(users_level_coins):
                            if self.coins >= level_data.coins:
                                if index <= len(users_level_coins):
                                    next_level = users_level_coins[index - 1]
                                    self.level = next_level
                                    return self.level


    def _make_first_and_last_name(self):
        name = self.full_name.strip().split()
        self.first_name = name[0]
        self.last_name = name[1] if len(name) < 2 else 0

    def save(self, *args, **kwargs):
        self._make_first_and_last_name()
        if not self.pk:


            self.coins = 10

            exists_code = set(CustomUser.objects.values_list('user_code', flat=True))
            while True:
                characters = string.ascii_letters + string.digits
                code = ''.join(random.choices(characters, k=8))
                if code not in exists_code:
                    self.user_code = code
                    break
        super().save(*args, **kwargs)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }



