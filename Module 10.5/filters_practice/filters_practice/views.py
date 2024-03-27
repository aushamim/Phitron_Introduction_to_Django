from django.shortcuts import render


def home(requset):
    return render(requset, "index.html")
