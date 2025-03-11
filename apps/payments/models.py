from django.db import models

from apps.utils.models import BaseModel
from config import settings


class Order(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    tariff = models.ForeignKey('general.Tariff', on_delete=models.PROTECT)
    days  = models.IntegerField(default=0)
    expire_date = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Transaction(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    state = models.CharField(max_length=100)
    transaction_id = models.IntegerField()

    def __str__(self):
        return self.state
