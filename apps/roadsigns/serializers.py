from rest_framework import serializers
from apps.roadsigns.models import RoadSign

class RoadSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSign
        fields = '__all__'