from django.contrib import admin

from apps.general.models import Tariff, Discount


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    pass

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass