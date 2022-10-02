from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("write/", views.write, name="write"),
    path("detail/<int:_id>", views.detail, name="detail"),
    path("delete/<int:_id>", views.delete, name="delete"),
    path("update/<int:_id>", views.update, name="update"),
]
