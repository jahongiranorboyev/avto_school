from rest_framework import serializers

from apps.general.models import report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = report.Report
        fields = '__all__'
        read_only_fields = ('created_at','created_by','updated_at','updated_by')