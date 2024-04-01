from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, FormView
from django.contrib.auth.decorators import login_required

from car_manage.models import BoughtCar
from user_manage.forms import ChangeUserInfoForm, SignUpForm


# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "user_manage_form.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Account Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create an account"
        return context


class Login(LoginView):
    template_name = "user_manage_form.html"

    def get_success_url(self):
        return reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Please Login"
        return context


class Logout(LogoutView):

    def get_success_url(self):
        messages.success(self.request, "Logged Out Successfully")
        return reverse_lazy("home")


@login_required
def profile(request):
    bought_cars = BoughtCar.objects.filter(user=request.user)
    return render(
        request, "profile.html", {"user": request.user, "bought_cars": bought_cars}
    )


@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = ChangeUserInfoForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile Edited Successfully")
            return redirect("profile")
    else:
        profile_form = ChangeUserInfoForm(instance=request.user)
    return render(
        request,
        "user_manage_form.html",
        {"title": "Edit User Information", "form": profile_form},
    )
