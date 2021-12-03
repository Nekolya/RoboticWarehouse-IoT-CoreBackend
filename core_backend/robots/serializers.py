from products.serializers import ProductSerializer
from products.models import Product
from .models import Robot, RobotStatus
from rest_framework import serializers
from products.views import ProductGetSerializer

class RobotStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotStatus
        fields = '__all__'

class RobotGetSerializer(serializers.ModelSerializer):
    status = RobotStatusSerializer()
    product = ProductSerializer()
    class Meta:
        model = Robot
        fields = '__all__'



class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'
