from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.foods),
    path("/home", views.foods),
]
