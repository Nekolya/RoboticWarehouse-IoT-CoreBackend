from rest_framework import viewsets, mixins, status, generics
from .serializers import (Robot, RobotSerializer,
                          RobotStatus, RobotStatusSerializer)


class RobotViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotStatusViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = RobotStatus.objects.all()
    serializer_class = RobotStatusSerializer
