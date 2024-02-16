from django.urls import include, path

urlpatterns = [
    path("projects/", include("api.v1.projects.urls")),
]
