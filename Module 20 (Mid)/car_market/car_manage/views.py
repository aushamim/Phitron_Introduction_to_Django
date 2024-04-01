from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from car_manage.forms import CommentForm
from car_manage.models import BoughtCar, Car


# Create your views here.
class CarDetails(DetailView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "car_details.html"

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car_data = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car_data
            new_comment.save()
            messages.success(self.request, "New Comment Added")
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_data = self.object
        comments = car_data.comments.all()
        comment_form = CommentForm()
        context["comments"] = comments
        context["comment_form"] = comment_form
        return context


@login_required
def buy_car(request, id):
    car_data = Car.objects.get(pk=id)
    user = request.user
    BoughtCar.objects.create(user=user, car=car_data)
    car_data.quantity -= 1
    car_data.save()
    messages.success(request, f"Successfully Bought - {car_data}")
    return redirect("profile")
