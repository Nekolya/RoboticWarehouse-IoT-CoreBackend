from rest_framework import viewsets, mixins, status, generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from .serializers import (LocationType, Area, Location,
                          AreaSerializer, LocationTypeSerializer, LocationSerializer)


class LocationTypeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer


class AreaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class LocationViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
