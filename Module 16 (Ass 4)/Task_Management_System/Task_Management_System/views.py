from django.shortcuts import render

from task.models import Task


def home(request):
    task_data = Task.objects.all()
    return render(request, "home.html", {"task_data": task_data})
