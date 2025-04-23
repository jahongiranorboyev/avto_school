from django.urls import path

from apps.general import views


urlpatterns =[
    path('level/', views.LevelCreateListAPIView.as_view(), name='level-create-list'),
    path('report/',views.ReportListCreateAPIView.as_view(), name='report-create-list'),

]