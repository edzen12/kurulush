from rest_framework import generics, permissions, viewsets

from .models import Gallery
from . import serializers


class GalleryView(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = serializers.GallerySerializer


# class GalleryView(generics.ListAPIView):

#     serializer_class = GallerySerializer
#     queryset = Gallery.objects.all()



# class GalleryDetailView(generics.RetrieveAPIView):

#     serializer_class = GalleryDetailSerializer
#     queryset = Gallery.objects.all()

