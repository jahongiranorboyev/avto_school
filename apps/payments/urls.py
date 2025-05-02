from tkinter.font import names

from django.urls import path
from apps.payments import views
urlpatterns = [
    path('', views.PaymeWebhookAPIView.as_view(), name='payment-webhook'),
    path('<uuid:order_id>',views.PaymentLinkAPIView.as_view(), name='payment-link'),
    path('order-list/', views.OrderListAPIView.as_view(), name='order-list'),
    path('order-create/', views.OrderCreateAPIView.as_view(), name='order-create'),
    path('tariff-list/', views.TariffListAPIView.as_view(), name='tariff-create-list'),
]

