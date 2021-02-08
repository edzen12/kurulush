from rest_framework import viewsets
from .models import News
from . import serializers


class NewsListView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = serializers.NewsListSerializer


# class NewsListView(generics.ListAPIView):

#     serializer_class = NewsListSerializer
#     queryset = News.objects.all()


# class NewsDetailView(generics.RetrieveAPIView):

#     serializer_class = NewsDetailSerializer
#     queryset = News.objects.all()


