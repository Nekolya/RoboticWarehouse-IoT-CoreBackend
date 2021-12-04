import json

from os import stat
from rest_framework import viewsets, mixins, status, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from utils.find_way import bfs
from utils.robot_mqtt_post import publish
from zones.models import Area

from .serializers import (AuthUser, AuthUserSerializer, MyTokenRefreshSerializer,
                          Order, OrderSerializer, OrderGetSerializer, OrderStatus, OrderStatusSerializer,
                          SetRobotSerializer)

from robots.models import Robot, RobotStatus
from random import choice

# Create your views here.


class AuthUserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    # TODO return 404 or something
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        response = Response(
            {'access': serializer.validated_data['access']}, status=status.HTTP_200_OK)
        print(serializer.validated_data)
        response.set_cookie('refresh',
                            value=serializer.validated_data['refresh'],
                            max_age=60*60*24*30,
                            path='/',
                            secure=False,
                            httponly=True,
                            samesite='Strict')
        return response


class MyTokenRefreshView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    serializer_class = MyTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        try:
            if request.COOKIES.get('refresh'):
                refresh = RefreshToken(request.COOKIES.get('refresh'))
            else:
                return Response({'success': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        data = {'access': str(refresh.access_token)}

        refresh.set_jti()
        refresh.set_exp()

        response = Response(data, status=status.HTTP_200_OK)

        response.set_cookie('refresh',
                            value=str(refresh),
                            max_age=60*60*24*30,
                            path='/',
                            domain=None,
                            secure=False,
                            httponly=True,
                            samesite='Strict')
        return response


class LogoutView(generics.GenericAPIView):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    serializer_class = MyTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        print(request.user)
        # if request.user:

        response = Response({'success': 'ok'}, status=status.HTTP_200_OK)

        response.set_cookie('refresh',
                            value="",
                            max_age=0,
                            path='/',
                            secure=False,
                            httponly=True,
                            samesite='Strict')
        return response


class OrderStatusViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    queryset = Order.objects.all().order_by("id")
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return OrderSerializer
        return OrderGetSerializer


class SetRobot(generics.GenericAPIView):
    """
    Set robot to order
    if robot is null - set random
    """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = SetRobotSerializer
    
    def post(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        print(request.data)
        try:
            order = Order.objects.get(pk=request.data['order_id'])
        except Exception as e:
            print(e.args)
            return Response(status=status.HTTP_404_NOT_FOUND)
        robot = None
        if 'robot_id' in request.data:
            robot = request.data['robot_id']

        if robot:
            try:
                robot = Robot.objects.get(pk=request.data['order_id'])
                if robot.status.id == 1 or robot.status.id == 2 and robot.charge > 10:
                    
                    product = order.product
                    target = product.location.area.id
                    way = bfs(robot.area.id, target)
                    b = bfs(target, 5)
                    way.extend(b)
                    c = bfs(5, 13)
                    way.extend(c)
                    print(way)
                    area = robot.area.id
                else:
                    # data={"error": "This robot unavailible"}
                    return Response(status=status.status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e.args)
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                robots = list(Robot.objects.filter(status__id=1))
                print(robots)
                robot  = choice(robots)
                product = order.product
                target = product.location.area.id
                way = bfs(robot.area.id, target)
                b = bfs(target, 5)
                way.extend(b)
                c = bfs(5, 13)
                way.extend(c)
                print(way)
            except:
                # data={"error": "All robots unavailible"}, 
                return SetRobotSerializer(data={"robot_id": robot.id, "order_id": order.id})
        serializer = SetRobotSerializer(data={"robot_id": robot.id, "order_id": order.id})
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            return Response(status=status.status.HTTP_400_BAD_REQUEST)
        order.robot = robot
        order.save()
        robot.status = RobotStatus.objects.get(pk=5)
        robot.save()
        publish("robots/tasks", json.dumps({
            "id":robot.id, 
            "way": way,
            "order": order.id
        }))
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
