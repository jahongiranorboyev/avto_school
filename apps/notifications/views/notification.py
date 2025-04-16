<<<<<<< HEAD
=======
class UserAllNotification(APIView):
    authentication_class = (JWTAuthentication,)

    class get(self, request):
        user_id = request.user.id
        queryset = UserNotification.objects.filter(user_id=user_id, is_read=False)
        serializer = UserNotificationSerializer(queryset, many=True)
        return Response("result": {
            'notifications': serializer.data
        })
>>>>>>> 2061695 (natofications and books apps changed)

