from rest_framework import viewsets, mixins

from . import serializers
from .models import Product, Category


class ProductListView(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet, ):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer


class CategoryListView(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet,):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
