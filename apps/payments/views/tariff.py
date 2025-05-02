from rest_framework import generics

from apps.general.models import General
from apps.payments.models import Tariff, Order
from apps.payments.serializers import TariffSerializer
from rest_framework.permissions import IsAuthenticated


class TariffListAPIView(generics.ListAPIView):
    """
       API view to list available Tariffs with optional context
       for applying coupons, discounts, or user-specific orders.
    """
    serializer_class = TariffSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
            Returns Tariff queryset ordered by creation time and
            prefetches related discount object to avoid N+1 queries.
        """
        return Tariff.objects.select_related('discount').order_by('created_at')

    def get_serializer_context(self):
        """
           Provides additional context to the serializer, such as:
           - mode: determines how pricing fields are included
           - general_obj: system-wide settings or coupons
           - user_order: the user's active unpaid order

           These are included only when relevant (e.g., in 'coupon' mode).
        """
        context = super().get_serializer_context()
        request = self.request
        user = request.user
        mode = request.query_params.get('mode', 'default')
        context['mode'] = mode
        if mode == 'coupon' and user.is_authenticated:

            general_obj = General.objects.first()
            user_order = Order.objects.filter(user=user, is_paid=False, coupon_code__isnull=False).only(
                'coupon_code', 'created_at', 'is_paid'
            ).first()
            context.update({
                'general_obj': general_obj,
                'user_order': user_order

            })
        return context
