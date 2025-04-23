from django.contrib import admin

from apps.general.models import *




@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'coins')
    list_filter = ('coins',)
    search_fields = ('title',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('user','lesson','question','report_type','reason')
    list_filter = ('user','lesson','question','report_type')
    search_fields = ('user',)