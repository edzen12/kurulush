from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'product', views.ProductListView, basename="product")
router.register(r'category', views.CategoryListView, basename="category")
urlpatterns = router.urls

