from django.urls import path
from apps.payments.views import PaymeWebhookAPIView,PaymentLinkAPIView
urlpatterns = [
    path('',PaymeWebhookAPIView.as_view(), name='payment-webhook'),
    path('<uuid:order_id>',PaymentLinkAPIView.as_view(), name='payment-link'),
]