from rest_framework import serializers

from apps.roadsigns.models import RoadSign

class RoadSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSign
        fields = '__all__'
        read_only_fields = ('id','created_at','created_by','updated_at','updated_by')