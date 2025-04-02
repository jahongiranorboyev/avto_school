from django.contrib import admin

from apps.roadsigns.models import RoadSign


admin.site.register(RoadSign)
class RoadSignAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'parent', 'ordering')
    list_filter = ('parent', 'created_at')
    search_fields =  ('title')
