from django.urls import path

from solf.apps.classes.api import views

urlpatterns = [
    path(
        "",
        views.ClassViewSet.as_view({"get": "list"}),
        name="class-list",
    ),
    path(
        "<int:pk>/",
        views.ClassViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="class-details",
    ),
    path(
        "schedule/",
        views.ClassScheduleViewSet.as_view({"get": "list"}),
        name="class-schedule-list",
    ),
    path(
        "schedule/<int:pk>/",
        views.ClassScheduleViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="class-schedule-details",
    ),
    path(
        "schedule/<int:pk>/sign-up/",
        views.ClassScheduleViewSet.as_view(
            {
                "post": "sign_up",
            }
        ),
        name="class-schedule-sign-up",
    ),
    path(
        "logs/",
        views.ClassLogViewSet.as_view({"get": "list"}),
        name="class-logs-list",
    ),
    path(
        "logs/<int:pk>/",
        views.ClassLogViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="class-logs-details",
    ),
    path(
        "entries/my",
        views.ClassEntryViewSet.as_view({"get": "list"}),
        name="class-logs-list",
    ),
]
