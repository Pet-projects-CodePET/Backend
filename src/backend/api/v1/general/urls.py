from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.general.views import (
    CounterApiView,
    SectionViewSet,
    SkillViewSet,
    SpecialistViewSet,
)

router = DefaultRouter()
router.register("specialists", SpecialistViewSet, basename="specialists")
router.register("skills", SkillViewSet, basename="skills")

urlpatterns = [
    path("section/", SectionViewSet.as_view({"get": "list"})),
    path("counter/", CounterApiView.as_view()),
    path("", include(router.urls)),
]
