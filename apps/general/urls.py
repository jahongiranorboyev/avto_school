from django.urls import path

from apps.general.views import report,level,tareff


urlpatterns = [
    path('report/',report.ReportListCreateAPIView.as_view(), name='report-list-create'),
    path('level/',level.LevelListCreateAPIView.as_view(), name='level-list-create'),
    path('tareff/',tareff.TariffListCreateAPIView.as_view(), name='tareff-list-create'),

]

