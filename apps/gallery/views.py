from rest_framework import generics, permissions, viewsets

from .models import Gallery
from . import serializers


class GalleryView(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = serializers.GallerySerializer

