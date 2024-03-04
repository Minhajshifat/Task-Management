from django.urls import path, include
from . import views


urlpatterns = [
    path("registation/", views.signup, name="registation"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.userLogout, name="logout"),
    path(
        "active/<uid64>/<token>/",
        views.activate,
        name="activate",
    ),
]
