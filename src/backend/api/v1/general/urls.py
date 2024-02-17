from django.urls import include, path

from apps.general.views import CounterApiView

urlpatterns = [
    path("counter", CounterApiView.as_view()),
]
