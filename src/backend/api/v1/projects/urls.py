from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectPreviewViewSet, ProjectViewSet

router_v1 = DefaultRouter()

router_v1.register(
    "preview_main", ProjectPreviewViewSet, basename="projects-preview"
)
router_v1.register("", ProjectViewSet, basename="projects")
urlpatterns = [
    path("", include(router_v1.urls)),
]
