from django.urls import path

from apps.general.views import tariff,level,report


urlpatterns =[
    path('tariff/', tariff.TariffListCreateAPIView.as_view(), name='tariff-create-list'),
    path('level/', level.LevelCreateListAPIView.as_view(), name='level-create-list'),
    path('report/',tariff.TariffListCreateAPIView.as_view(), name='report-create-list'),

]