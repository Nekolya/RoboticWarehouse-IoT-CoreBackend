from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# router.register(r'users', views.EditableTextViewSet)
router.register(r'locations-types', views.LocationTypeViewSet)
router.register(r'areas', views.AreaViewSet)
router.register(r'locations', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]