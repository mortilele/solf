from django.urls import path

from solf.apps.common.api import views

urlpatterns = [
    path(
        "cities/",
        views.CityViewSet.as_view({"get": "list"}),
        name="city-list",
    ),
    path(
        "cities/<int:pk>/",
        views.CityViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="city-details",
    ),
]
