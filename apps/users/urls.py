from django.urls import path
from apps.users import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('edit-profile/<str:pk>/', views.EditProfileAPIView.as_view(), name='edit-profile'),
    path('support/create/', views.SupportAPIView.as_view(), name='support-name'),
    path('support/report-choices/', views.ReportChoicesAPIView.as_view(), name='report-choices'),
    path('promo-code/<str:pk>/', views.PromoCodeRetrieveAPIView.as_view(), name='promo-code'),
]

