from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.allblog, name="allblog"),
    path("<int:blog_id>", views.details, name="details"),
]