from rest_framework import viewsets, mixins, status, generics
from .serializers import (Product, ProductSerializer,
                          Category, CategorySerializer)


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
