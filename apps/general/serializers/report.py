from rest_framework import serializers

from apps.general.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('created_at','created_by','updated_at','updated_by')