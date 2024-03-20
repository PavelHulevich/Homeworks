from django.shortcuts import render
from django.views import View
from .models import Tasks

class TaskView(View):
    def get(self, request, *args, **kwargs):
        tasks_id = kwargs.get('task_id')
        task = Tasks.objects.get(pk=tasks_id)
        return render(request, 'tasks/show.html', context={
            'task': task,
        })


class TaskAllView(View):
    def get(self, request, *args, **kwargs):
        task = Tasks.objects.all()[:15]
        return render(request, 'tasks/show_all.html', context={
            'task': task,
        })


class TaskFileView(View):
    def get(self, request, *args, **kwargs):
        tasks_id = kwargs.get('task_id')
        task = Tasks.objects.get(pk=tasks_id)
        return render(request, 'tasks/show_file.html', context={
            'task': task,
        })