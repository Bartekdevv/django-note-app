from django.urls import path, include
from . import views

app_name = "note"
urlpatterns = [
    path("", views.redirect),
    path("home/", views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("create/", views.new_note, name="new_note"),
    path("logout/", views.logout_view, name="logout_view"),
]
