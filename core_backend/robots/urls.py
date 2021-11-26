from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# router.register(r'users', views.EditableTextViewSet)
router.register(r'robots', views.RobotViewSet)
router.register(r'robots-statuses', views.RobotStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]