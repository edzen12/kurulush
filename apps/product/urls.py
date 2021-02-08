from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = DefaultRouter()
router.register(r'api/product', views.ProductListView, basename="product")
urlpatterns = router.urls

