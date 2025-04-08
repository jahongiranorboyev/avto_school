from rest_framework import serializers

from apps.general.models import Level
from apps.general.serializers.level import LevelSerializer
from apps.users.models import CustomUser





class UserListSerializer(serializers.ModelSerializer):
    level = LevelSerializer()
    total_questions = serializers.SerializerMethodField()


    def get_total_questions(self, obj):
        return self.context.get('total_questions', 0)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        level = data.get('level', {})
        coins = data.get('coins', 0)
        if level and 'coins' in level:
            current_level_coins = level['coins']

            next_level = Level.objects.filter(coins__gt=current_level_coins).order_by('coins').first()

            if next_level:
                next_level_coins = next_level.coins
                remaining_coins = current_level_coins - coins

                if remaining_coins > 0:
                    percentage = (remaining_coins / (next_level_coins - current_level_coins)) * 100
                    level['percentage'] = round(percentage, 2)
                else:
                    level['percentage'] = 100

            data['level'] = level

        return data


