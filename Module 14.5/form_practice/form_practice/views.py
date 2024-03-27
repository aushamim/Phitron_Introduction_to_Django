from django.shortcuts import render

from form.forms import basicForm


def home(request):
    return render(request, "home.html")


def formView(request):
    form = basicForm()
    return render(request, "form/form.html", {"form": form})
