from rest_framework import generics

from apps.payments.models import Order
from apps.payments.serializers import OrderSerializer


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer


    def get_queryset(self):
        """
            Returns Order queryset ordered by creation time and
            prefetches related discount object to avoid N+1 queries.
        """
        return Order.objects.select_related('tariff', 'user').order_by('created_at')
