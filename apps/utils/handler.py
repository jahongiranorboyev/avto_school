from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    res = exception_handler(exc, context)
    if res is not None:
        data ={
            'status':'error',
            'code': res.status_code,
            'message': res.data,
        }
        res.data = data
    else:
        data ={
            'status':'error',
            'code': 500,
            'message': str(exc),
        }
        res = Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return res


