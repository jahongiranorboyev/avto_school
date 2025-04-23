from rest_framework import serializers


class UserBalanceSerializer(serializers.Serializer):
    balance = serializers.IntegerField()

    class Meta:
        fields = ['balance']

