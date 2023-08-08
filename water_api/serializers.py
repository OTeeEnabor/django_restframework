from rest_framework import serializers
from .models import WaterQuality
class WaterQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterQuality
        fields = '__all__'
        