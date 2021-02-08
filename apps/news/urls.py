from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = DefaultRouter()
router.register(r'api/news', views.NewsListView, basename="news")
urlpatterns = router.urls


# urlpatterns = [
#     path("news/", views.NewsListView.as_view()),
#     path("news/<int:pk>/", views.NewsDetailView.as_view()),
# ]
