from django.urls import path
from . import views

app_name = "appapp"

urlpatterns = [
    path("", views.index, name="index"),
]
