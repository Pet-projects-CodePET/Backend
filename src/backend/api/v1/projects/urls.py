from django.urls import path

from api.v1.projects.views import (
    AddFavoriteProject,
    UserFavoriteProjectsListAPIView,
)


urlpatterns = [
    path("add_favorite_project", AddFavoriteProject.as_view()),
    path("favorite_projects_list", UserFavoriteProjectsListAPIView.as_view()),
]
