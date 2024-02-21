from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectPreviewMainViewSet, ProjectViewSet

router_v1 = DefaultRouter()

router_v1.register(
    "preview_main", ProjectPreviewMainViewSet, basename="projects-preview-main"
)
router_v1.register("", ProjectViewSet, basename="projects")
urlpatterns = [
    path("", include(router_v1.urls)),
]
