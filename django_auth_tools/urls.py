from django.urls import path

from . import views

app_name = "django_auth_tools"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("public/", views.PublicView.as_view(), name="public"),
]
