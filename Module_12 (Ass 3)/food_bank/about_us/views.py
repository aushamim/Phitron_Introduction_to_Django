from django.shortcuts import render


def about(requset):
    return render(requset, "about_us/index.html")
