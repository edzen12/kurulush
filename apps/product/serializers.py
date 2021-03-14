from rest_framework import serializers

from .models import Product, Category


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    
    class Meta:
        model = Product
        fields = "__all__"

