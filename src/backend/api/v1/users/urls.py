from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.users.views import CustomUserViewSet

router = DefaultRouter()
router.register(r"users", CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
