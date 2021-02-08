from django.urls import path   
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = DefaultRouter()
router.register(r'api/gallery', views.GalleryView, basename="gallery")
urlpatterns = router.urls

# urlpatterns = [
#     path("gallery/", views.GalleryView.as_view()),
#     path("gallery/<int:pk>/", views.GalleryDetailView.as_view()),
# ]
