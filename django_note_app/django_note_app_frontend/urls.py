from django.urls import path, include
from . import views


app_name = "note"
urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.new_note, name="new_note"),
]
