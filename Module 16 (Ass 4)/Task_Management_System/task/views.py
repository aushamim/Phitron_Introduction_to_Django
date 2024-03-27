from django.shortcuts import redirect, render

from task.forms import TaskForm
from task.models import Task


# Create your views here.
def add_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("home")
    else:
        task_form = TaskForm()
    return render(request, "task/task.html", {"form": task_form})


def edit_task(request, id):
    task = Task.objects.get(pk=id)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("home")
    else:
        task_form = TaskForm(instance=task)
    return render(request, "task/task.html", {"form": task_form})


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect("home")
