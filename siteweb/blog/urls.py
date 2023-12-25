from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:slug_name>/", views.read_article, name="read_article")
]
