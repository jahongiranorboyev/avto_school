from django.contrib import admin

from apps.payments.models import Order, Transaction, Tariff

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'id',
        'is_paid',
        'user_id',
        'user_balance',
        'user_full_name',
        'tariff_id',
        'tariff_price',
        'price',
        'discount_price',
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user', 'tariff')

    def user_id(self, obj):
        return obj.user.id

    def user_balance(self, obj):
        return obj.user.balance

    def user_full_name(self, obj):
        return obj.user.full_name

    def tariff_id(self, obj):
        return obj.tariff.id

    def tariff_price(self, obj):
        return obj.tariff.price


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
