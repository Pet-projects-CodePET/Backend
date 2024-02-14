from typing import List

from django.contrib import admin
from django.urls import include, path

urlpatterns: List[str] = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.v1.urls")),
    path("general/v1/", include("apps.general.urls")),
]
