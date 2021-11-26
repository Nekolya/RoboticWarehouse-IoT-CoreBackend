from .models import Robot, RobotStatus
from rest_framework import serializers


class RobotStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotStatus
        fields = '__all__'


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'
