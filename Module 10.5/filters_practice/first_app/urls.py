from django.urls import path

from first_app import views


urlpatterns = [
    path("", views.home),
    path("home/", views.home),
]
