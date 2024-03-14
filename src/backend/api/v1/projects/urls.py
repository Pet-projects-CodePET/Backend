from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.projects.views import (
    DirectionViewSet,
    ProjectPreviewMainViewSet,
    ProjectViewSet,
)

router = DefaultRouter()

router.register(
    "preview_main", ProjectPreviewMainViewSet, basename="projects-preview-main"
)
router.register("directions", DirectionViewSet, basename="projects-directions")
router.register("", ProjectViewSet, basename="projects")


urlpatterns = [
    path("", include(router.urls)),
]
