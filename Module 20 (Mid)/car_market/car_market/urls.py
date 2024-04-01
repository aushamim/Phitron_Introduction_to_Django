from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from car_market import settings, views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("filter/car/<slug:brand_slug>", views.home, name="brand-filter"),
    path("", include("user_manage.urls")),
    path("", include("car_manage.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
