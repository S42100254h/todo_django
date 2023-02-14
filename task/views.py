from django.shortcuts import redirect, render
from django.views.generic import View
from django.http.response import JsonResponse

from .forms import TaskForm
from .models import Task


class TaskView(View):
    def get(self, request):
        if request.headers.get("Content-Type") == "application/json":
            tasks = Task.objects.values()
            tasks_list = list(tasks)
            return JsonResponse(tasks_list, safe=False, status=200)
        return render(request, "task_list.html")

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("task_list")
