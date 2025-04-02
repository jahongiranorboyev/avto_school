from rest_framework import generics

from apps.general.models.report import Report
from apps.general.serializers.report import ReportSerializer


class ReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
