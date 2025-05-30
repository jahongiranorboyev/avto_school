from django.utils import timezone

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.payments.models import Order, Transaction
from apps.utils.services.payments.check_payment_functions import validation



class PaymeWebhookAPIView(APIView):
    order = transaction = None
    authentication_classes = ()

    @validation
    def post(self, request):
        method = request.data['method']
        match method:
            case 'CheckPerformTransaction':
                data = {
                    "result": {
                        "allow": True
                    }
                }
            case 'CreateTransaction':
                transaction_id = request.data['params']['id']
                transaction, _ = Transaction.objects.get_or_create(id=transaction_id,
                                                                   defaults={'order_id': self.order.pk})
                data = {
                    "result": {
                        'create_time': int(transaction.create_at.timestamp() * 1000),
                        'transaction': request.data['params']['id'],
                        'state': Transaction.State.AWAITING_PAYMENT # 1
                    }
                }
            case 'CheckTransaction':
                data = {
                    "result": {
                        'create_time': self.transaction.get_created_time(),
                        'perform_time': self.transaction.get_perform_time(),
                        'cancel_time': self.transaction.get_cancel_time(),
                        'transaction': self.transaction.transaction_id,
                        'state': self.transaction.state,
                        'reason': self.transaction.reason,

                    }
                }
            case 'PerformTransaction':
                transaction_id = request.data['params']['id']
                self.transaction = Transaction.objects.get(id=transaction_id)
                if not self.transaction.performed_at:
                    self.transaction.performed_at = timezone.now()
                    self.transaction.state = Transaction.State.COMPLETED
                    self.transaction.save()
                    self.transaction.order.is_paid = True
                    self.transaction.save()
                data = {
                    "result": {
                        'perform_time': self.transaction.get_perform_time(),
                        'transaction': self.transaction.transaction_id,
                        'state': self.transaction.state,
                    }
                }
            case 'CancelTransaction':
                if not self.transaction.canceled_at:
                    self.transaction.canceled_at = timezone.now()
                    self.transaction.state = -1 * self.transaction.state
                    self.transaction.reason = request.data['params']['reason']
                    self.transaction.save()
                data = {
                    "result": {
                        'cancel_time': self.transaction.get_canceled_time(),
                        'transaction': self.transaction.transaction_id,
                        'state': self.transaction.state,
                    }
                }
            case _:
                data = {}

        return Response(data, status=status.HTTP_200_OK)
