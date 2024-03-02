from django.urls import path, include
from . import views


urlpatterns = [
    path("registation/", views.signup, name="registation"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.userLogout, name="logout"),
    path(
        "activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/",
        views.activate,
        name="activate",
    ),
]
