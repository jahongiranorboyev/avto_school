from rest_framework import serializers

from apps.general.models import Level
from apps.quizzes.models import Question
from apps.users.models import CustomUser, Support



class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


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


class EditProfileSerializer(serializers.Serializer):
    re_password = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    icon = serializers.ImageField(required=False, allow_null=True)
    first_name = serializers.CharField(max_length=30, required=False)

    def validate(self, attrs):
        request = self.context.get('request')
        password = attrs.get('password', '')
        re_password = attrs.get('re_password', '')

        user = request.user
        if not user or not user.is_authenticated:
            raise serializers.ValidationError('User did not register')

        if password != re_password:
            raise serializers.ValidationError('Password and Re Password must be equal please check it')

        return attrs

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        icon = validated_data.get('icon', None)

        if icon:
            instance.icon = icon
        if password:
            instance.set_password(password)

        for attr, value in validated_data.items():
            if attr != 'password':
                setattr(instance, attr, value)

        instance.save()
        return instance


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'

