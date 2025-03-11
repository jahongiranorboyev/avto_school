from django.conf import settings
from django.db import models

from apps.utils.models import BaseModel


class General(BaseModel):
    user_code_discount = models.IntegerField(default=0)
    user_code_discount_is_percent = models.BooleanField(default=False)

    def __str__(self):
        return self.user_code_discount


class Report(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    question = models.ForeignKey('quizzes.Question', on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.question.title


class Level(BaseModel):
    title = models.CharField(max_length=100)
    icon = models.ImageField(null=True, blank=True)
    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Discount(BaseModel):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    is_percent = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Tariff(BaseModel):
    title = models.CharField(max_length=100)
    days = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    discount = models.ForeignKey('general.Discount', on_delete=models.PROTECT)

    def __str__(self):
        return self.title



