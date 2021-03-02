from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from .models import Product, Category


class ProductListView(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet, ):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class CategoryListView(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet,):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
