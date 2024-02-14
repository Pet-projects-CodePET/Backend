from django.urls import include, path

from apps.general.views import CounterApiView

urlpatterns = [
    path("getcounter", CounterApiView.as_view()),
]
