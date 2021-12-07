from rest_framework import viewsets, mixins, status, generics
from .serializers import (Product, ProductSerializer, ProductGetSerializer,
                          Category, CategorySerializer)


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = Product.objects.all()
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ProductSerializer
        return ProductGetSerializer
    


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrIsOwner|AdminOrPost]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
