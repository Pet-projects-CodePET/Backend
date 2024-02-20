from django.urls import include, path

urlpatterns = [
    path("", include("api.v1.users.urls")),
    path("", include("djoser.urls.authtoken")),
    path("", include("api.v1.general.urls")),
]
