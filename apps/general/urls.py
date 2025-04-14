from django.urls import path

from apps.general.views import level,report


urlpatterns =[
    path('level/', level.LevelCreateListAPIView.as_view(), name='level-create-list'),
    path('report/',report.ReportListCreateAPIView.as_view(), name='report-create-list'),

]