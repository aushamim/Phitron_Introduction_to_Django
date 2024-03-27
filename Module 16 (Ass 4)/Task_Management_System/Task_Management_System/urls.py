from django.contrib import admin
from django.urls import include, path

from Task_Management_System import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("task/", include("task.urls")),
    path("category/", include("category.urls")),
]
