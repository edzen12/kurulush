from rest_framework import viewsets
from .models import Product
from . import serializers


class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer

