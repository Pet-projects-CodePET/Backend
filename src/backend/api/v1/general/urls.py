from django.urls import path

from api.v1.general.views import CounterApiView, SectionViewSet

urlpatterns = [
    path("section", SectionViewSet.as_view({"get": "list"})),
    path("counter", CounterApiView.as_view()),
]
