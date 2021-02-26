from rest_framework import viewsets
from .models import Product, Category
from . import serializers


class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer

class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
