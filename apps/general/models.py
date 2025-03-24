from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _, get_language

# from apps.utils.models import BaseModel


# class General(BaseModel):
#     user_code_discount = models.IntegerField(
#         validators=[MinValueValidator(0)],
#         default=0
#     )
#     user_code_discount_is_percent = models.BooleanField(default=False)
#
#
#     def __str__(self):
#         return self.user_code_discount


# class Report(BaseModel):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         verbose_name=_('User'),
#     )
#     lesson = models.ForeignKey(
#         to='lessons.Lesson',
#         on_delete=models.PROTECT,
#         verbose_name=_('Lesson'),
#     )
#     question = models.ForeignKey(
#         to='quizzes.Question',
#         on_delete=models.PROTECT,
#         verbose_name=_('Question'),
#     )
#     report_type = models.CharField(
#         max_length=100,
#         verbose_name=_('Report type'),
#     )
#     reason = models.CharField(
#         max_length=100,
#         verbose_name=_('Reason'),
#     )
#
#     def __str__(self):
#         return self.question.title


# class Level(BaseModel):
#     title = models.CharField(
#         max_length=100,
#         verbose_name=_('Title'),
#     )
#     icon = models.ImageField(
#         null=True,
#         blank=True,
#         verbose_name=_('Icon'),
#         upload_to='icons/images/%Y/%m/%d/'
#
#     )
#     coins = models.IntegerField(
#         default=0,
#         verbose_name=_('Coins'),
#     )
#
#     def __str__(self):
#         return self.title

# class Discount(BaseModel):
#     name = models.CharField(
#         max_length=100,
#         verbose_name=_('Name'),
#     )
#     amount = models.IntegerField(
#         default=0,
#         validators=[MinValueValidator(0)],
#         verbose_name=_('Amount'),
#     )
#     is_percent = models.BooleanField(
#         default=False,
#         verbose_name=_('Is percent'),
#     )
#
#
#     def __str__(self):
#         return self.name

# class Tariff(BaseModel):
#     title = models.CharField(
#         max_length=100,
#         verbose_name=_('Title'),
#     )
#     days = models.IntegerField(
#         default=0,
#         verbose_name=_('Days'),
#     )
#     price = models.IntegerField(
#         default=0,
#         verbose_name=_('Price'),
#     )
#     discount = models.ForeignKey(
#         to='general.Discount',
#         on_delete=models.PROTECT,
#         verbose_name=_('Discount'),
#     )
    # 
    # def __str__(self):
    #     return self.title





