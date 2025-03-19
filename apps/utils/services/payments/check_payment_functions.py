from rest_framework.response import Response

from apps.utils.services.payments.payment_functions import *

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
