from rest_framework import viewsets
from .models import News
from . import serializers


class NewsListView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = serializers.NewsListSerializer

