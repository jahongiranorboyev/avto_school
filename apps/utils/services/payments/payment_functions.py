import base64

from django.conf import settings
from apps.payments.models import Order, Transaction


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
