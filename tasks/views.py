from django.http.response import HttpResponseRedirect
from django.shortcuts import render

tasks = []
# Add all your views here


def add_task(request):
    todo = request.GET.get("task")
    tasks.append({"todo": todo, "is_completed": False})
    return HttpResponseRedirect("/tasks")


def complete_task(request, index):
    todo = tasks[index-1]
    todo["is_completed"] = True
    return HttpResponseRedirect("/tasks")


def delete_task(request, index):
    del tasks[index-1]
    return HttpResponseRedirect("/tasks")


def task_view(request):
    return render(request, "task.html", {"path": "pending_tasks", "tasks": filter(lambda t: not t.get("is_completed"), tasks)})


def home_view(request):
    return render(request, "task.html", {"path": "all_tasks", "tasks": tasks})


def completed_task_view(request):
    return render(request, "task.html", {"path": "completed_tasks", "tasks": filter(lambda t: t.get("is_completed"), tasks)})
