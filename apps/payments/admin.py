from django.contrib import admin

from apps.payments.models import Order, Transaction


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass