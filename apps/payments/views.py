<<<<<<< HEAD
from django.utils import timezone

=======
import base64

from django.conf import settings
from django.utils import timezone
from django.utils.translation import get_language

>>>>>>> b6888bd (quizzes done !)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

<<<<<<< HEAD
from apps.general.models import Tariff
from apps.payments.models import Order, Transaction
from apps.utils.services.payments.generate_url import generate_payment_url
from apps.utils.services.payments.check_payment_functions import validation
=======
from apps.payments.models import Order, Transaction
from apps.general.models import Tariff


def generate_payment_url(order):
    params = (f'm={settings.PAYME_CASH_BOX_ID};'
              f'ac.order_id={order.pk};'
              f'a={order.pk}; '
              f'l={get_language()}; '
              f'c=https://fcf4-94-158-57-109.ngrok-free.app; '
              f'ct=1212; '
              f'ct=UZS'
              )
    params = base64.b64encode(params.encode()).decode()
    return f'https://checkout.paycom.uz/?{params}'
>>>>>>> b6888bd (quizzes done !)


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

<<<<<<< HEAD
=======
def check_auth(view, request):
    token = request.headers.get('Authorization')
    token = token.split()[-1]
    decoded = base64.b64decode(token).decode()
    login, password = decoded.split(':')
    assert login == 'Paycom' and password == settings.PAYME_CASH_BOX_TEST_KEY, 'Authentication failed'

def check_order(view, request):
    order_id = request.data['params']['account']['order_id']
    view.order = Order.objects.get(id=order_id)

def check_amount(view, request):
    order_id = request.data['params']['account']['order_id']
    amount = request.data['params']['amount']
    order = Order.objects.get(id=order_id)
    assert order.price * 100 == amount, 'Amount does not match'


def check_create_transaction(view, request):
    transaction_id = request.data['params']['id']
    order_id = request.data['params']['account']['order_id']
    if Transaction.objects.filter(order_id=order_id).exclude(id=transaction_id).exists():
        raise ValueError('Transaction already exists')


def check_transaction(view, request):
    if request.data['method'] == 'CheckTransaction':
        transaction_id = request.data['params']['id']
        view.transaction = Transaction.objects.filter(id=transaction_id)


def check_perform_transaction(view, request):
    if request.data['method'] == 'CheckPerformTransaction':
        order_id = request.data['params']['account']['order_id']
        Order.objects.get(id=order_id)

def check_cancel_transaction(view, request):
    if request.data['method'] == 'CancelTransaction':
        transaction_id = request.data['params']['id']
        view.transaction = Transaction.objects.filter(id=transaction_id)


def validation(func):
    def wrapper(view, request, *args, **kwargs):
        # ==================auth check ===================
        try:
            check_auth(view, request)
        except Exception as e:
            data = {
                "error": {
                    "code": -32504,
                    "message": str(e),
                },
            }
            return Response(data, status=200)
        # ==================order check ===================
        try:
            check_order(view, request)
        except Exception as e:
            data = {
                "error": {
                    "code": -31050,
                    "message": str(e),
                },
            }
            return Response(data, status=200)
        # ==================check  amount ===================
        try:
            check_amount(view, request)
        except Exception as e:
            data = {
                "error": {
                    "code": -31001,
                    "message": str(e),
                },
            }
            return Response(data, status=200)
        #==================check perform transaction ===================
        try:
            check_perform_transaction(view, request)
        except Exception as e:
            print('hi')
            data = {
                "error": {
                    "code": -31050,
                    "message": str(e),
                },
            }
            return Response(data, status=200)

        #==================check create transaction ===================
        try:
            check_create_transaction(view, request)
        except Exception as e:
            data = {
                "error": {
                    "code": -31050,
                    "message": str(e),
                },
            }
            return Response(data, status=200)
        # ==================check transaction ===================
        try:
            check_transaction(view, request)
        except Exception as e:
            data = {
                "error": {
                    "code": -31050,
                    "message": str(e),
                },
            }
            return Response(data, status=200)
        # ==================check cancel transaction ===================
        try:
            check_cancel_transaction(view, request)
        except Exception as e:
            data = {
                "error": {
                    "code": -31003,
                    "message": str(e),
                },
            }
            return Response(data, status=200)

        return func(view, request, *args, **kwargs)

    return wrapper

>>>>>>> b6888bd (quizzes done !)

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
