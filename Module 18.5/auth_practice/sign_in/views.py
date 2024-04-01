from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from sign_in.forms import SignUpForm


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect("profile")
    else:
        form = SignUpForm()
    return render(request, "sign_in.html", {"title": "Create an Account", "form": form})


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged In Successfully")
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "sign_in.html", {"title": "Please Login", "form": form})


def sign_out(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("home")
