from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewset(viewsets.ViewSet):
    """
    A simpleviewset for the category
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request, *args, **kwargs):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewset(viewsets.ViewSet):
    """
    This is a basics brand view
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, resquest, *args, **kwargs):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewset(viewsets.ViewSet):
    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, resquest, *args, **kwargs):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
