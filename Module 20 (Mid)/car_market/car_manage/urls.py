from django.urls import path
from car_manage import views


urlpatterns = [
    path("car-details/<int:id>", views.CarDetails.as_view(), name="car-details"),
    path("buy-car/<int:id>", views.buy_car, name="buy-car"),
]
