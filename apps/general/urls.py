from django.urls import path

from apps.general.views import report


urlpatterns = [
    path('report/',report.ReportListCreateAPIView.as_view(), name='report-list-create'),
]

