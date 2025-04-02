from rest_framework import serializers

from apps.general.models.report import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('id','created_at','updated_at','created_by','updated_by')