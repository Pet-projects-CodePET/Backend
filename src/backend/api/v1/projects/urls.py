from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet

router_v1 = DefaultRouter()
router_v1.register(
    "projects/preview", ProjectViewSet, basename="project-preview"
)

urlpatterns = [
    path("", include(router_v1.urls)),
]
