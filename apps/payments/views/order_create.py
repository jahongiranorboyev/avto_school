from rest_framework import generics

from apps.payments.models import Order
from apps.payments.serializers import OrderCreateSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer


    def get_queryset(self):
        """
            Returns Order queryset ordered by creation time and
            prefetches related discount object to avoid N+1 queries.
        """
        return Order.objects.select_related('tariff', 'user').order_by('created_at')
