# from fcm_django.models import FCMDevice
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
#
# from firebase_admin.messaging import Message, Notification,
# from django.utils.translation import gettext as _


import firebase_admin
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from firebase_admin import credentials

def post():
    messages = []
    for device in FCMDevice.objects.select_related('user').all()
        match device.user.lang:
            case 'eng':
                title = "hello"
                body = "you have a new message"
            case 'ru':
                title = "привет"
                body = "y вас есть новое сообщение"
            case 'uz':
                title = "salom"
                body = "sizda yangi xabar bor"

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=device.registration_id,
    )

    user = device.user
        match user.lang:
            case 'eng':
                title = "Hello"
                body = "You have a new message"
            case 'ru':
                title = "Привет"
                body = "У вас есть новое сообщение"
            case 'uz':
                title = "Salom"
                body = "Sizda yangi xabar bor"
            case _:
                title = "Hello"
                body = "You have a new message"
        try:
                response = messaging.send(message)
            print(f"Message sent to {user.username}: {response}")
        except Exception as e:
            print(f"Error sending to {user.username}: {e}")
