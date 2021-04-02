from django.urls import path

from solf.apps.core.api import views

urlpatterns = [
    path(
        "categories/",
        views.CategoryViewSet.as_view({"get": "list"}),
        name="category-list",
    ),
    path(
        "category/<int:pk>/",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="category-details",
    ),
]
