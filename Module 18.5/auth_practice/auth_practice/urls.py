from django.contrib import admin
from django.urls import include, path

from auth_practice import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("", include("sign_in.urls")),
    path("", include("user_profile.urls")),
]
