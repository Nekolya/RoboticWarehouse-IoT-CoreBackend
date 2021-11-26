from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import exceptions

from .models import AuthUser, OrderStatus, Order
import re


class AuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # email_sending()
        # if not re.match(r'^\S+@\S+$', validated_data['username']):
        #     raise serializers.ValidationError({'username': "Email error."})

        
        if re.match(r'^((?=.*\d)(?=.*\D)(?=.{8,}))', validated_data['password']):
            user = AuthUser.objects.create(
                username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()

            return user
        raise serializers.ValidationError({'password': "Password must contain at least 1 digit, 1 letter and be between 8-32 characters."})

    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'password']  # 'questionnaires'
        
class MyTokenRefreshSerializer(serializers.Serializer):
    def validate(self, attrs):
        return attrs
    
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
