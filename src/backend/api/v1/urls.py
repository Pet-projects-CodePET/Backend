from django.urls import include, path


urlpatterns = [
    path("", include("api.v1.projects.urls")),
]
