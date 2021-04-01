from django.urls import path

from solf.apps.business.api import views

urlpatterns = [
    path(
        "companies/",
        views.BusinessViewSet.as_view({"get": "list"}),
        name="business-list",
    ),
    path(
        "companies<int:pk>/",
        views.BusinessViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="business-details",
    ),

]
