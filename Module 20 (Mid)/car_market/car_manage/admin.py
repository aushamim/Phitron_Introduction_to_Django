from django.contrib import admin

from car_manage.models import BoughtCar, Brand, Car, Comment


# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(BoughtCar)
