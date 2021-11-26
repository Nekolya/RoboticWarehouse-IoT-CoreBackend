from rest_framework import viewsets, mixins, status, generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from .serializers import (AuthUser, AuthUserSerializer, MyTokenRefreshSerializer,
                          Order, OrderSerializer, OrderStatus, OrderStatusSerializer)

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
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
