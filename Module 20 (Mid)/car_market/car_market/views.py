from django.shortcuts import render

from car_manage.models import Brand, Car


def home(request, brand_slug=None):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    if brand_slug is not None:
        filter_brand = Brand.objects.get(slug=brand_slug)
        cars = Car.objects.filter(brand=filter_brand)
    return render(request, "home.html", {"cars": cars, "brands": brands})
