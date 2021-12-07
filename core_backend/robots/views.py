from rest_framework import viewsets, mixins, status, generics
from .serializers import (Robot, RobotSerializer, RobotGetSerializer,
                          RobotStatus, RobotStatusSerializer)


class RobotViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = Robot.objects.all()

    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return RobotSerializer
        return RobotGetSerializer


class RobotStatusViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = RobotStatus.objects.all()
    serializer_class = RobotStatusSerializer
