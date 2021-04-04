from django.urls import path

from solf.apps.users.api import views

urlpatterns = [
    path(
        "login/",
        views.LoginAPIView.as_view(),
        name="user-login",
    ),
    path(
        "",
        views.UserViewSet.as_view({"post": "create"}),
        name="user-create",
    ),
]
