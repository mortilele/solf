from django.urls import path

from solf.apps.core.api import views

urlpatterns = [
    path(
        "",
        views.CompanyViewSet.as_view({"get": "list"}),
        name="company-list",
    ),
    path(
        "<int:pk>/",
        views.CompanyViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="company-details",
    ),

]
