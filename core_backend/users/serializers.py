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
        fields = ['id', 'username', 'password', 'name', 'surename']  # 'questionnaires'
        
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
        
    def to_internal_value(self, data):
        # check for "finish_date": "" and convert to None
        # This must be done before .validate()
        try:
            if data['ordering_date'] == '':
                data['ordering_date'] = None
            if 'receiving_date' in data and data['receiving_date'] == '':
                data['finish_time'] = None
            if not data['language']:
                data['language'] = None
        except Exception as e:
            raise ValidationError('Bad data')
        return super(QuestionnairePostSerializer, self).to_internal_value(data)

class SetRobotSerializer(serializers.Serializer):
    robot_id = serializers.UUIDField(format='int', required=False)
    order_id = serializers.UUIDField(format='int', required=True)