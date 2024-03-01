from django.urls import path

from api.v1.profile.views import ProfileView

urlpatterns = [
    path("profile/<int:pk>", ProfileView.as_view()),
]
