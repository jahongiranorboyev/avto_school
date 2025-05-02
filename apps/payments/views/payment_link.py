from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.payments.models import Tariff
from apps.payments.models import Order
from apps.utils.services.payments.generate_url import generate_payment_url


class PaymentLinkAPIView(APIView):

    def post(self, request):
        user = request.user
        tariff_id = request.data['tariff_id']
        price = Tariff.objects.get(id=tariff_id).price
        days = Tariff.objects.get(id=tariff_id).days
        discount = Tariff.objects.get(id=tariff_id).discount

        order = Order.objects.create(
            user=user,
            price=price,
            days=days,
            discount_price=discount
        )
        url = generate_payment_url(order)
        return Response({'url': url}, status=status.HTTP_200_OK)
