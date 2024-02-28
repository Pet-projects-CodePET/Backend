from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.projects.views import FavoriteViewSet


router = DefaultRouter()
router.register(r"favorite", FavoriteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
