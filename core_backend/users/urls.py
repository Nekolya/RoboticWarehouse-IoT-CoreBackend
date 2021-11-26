from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

# router.register(r'users', views.EditableTextViewSet)
router.register(r'users', views.AuthUserViewSet)
router.register(r'orders-statuses', views.OrderStatusViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/refresh/', views.MyTokenRefreshView.as_view(),
         name='token_refresh'),
    path('auth/logout/', views.LogoutView.as_view(),
         name='token_refresh'),
]