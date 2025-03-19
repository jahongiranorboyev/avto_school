import base64

from django.conf import settings
from django.utils.translation import get_language


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