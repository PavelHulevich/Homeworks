from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import TaskForm
from .models import Tasks


# class TaskCreate(CreateView):
    # model = Tasks
    # fields = ['name', 'description']
    # success_url = reverse_lazy('tasks')
    # template_name = 'tasks/create2.html'
    # form_class = TaskForm

class TaskFormCreateView(View):
    def get(self, request,  *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create2.html',
                      {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TaskAllView')
        return render(request, 'tasks/create2.html', {'form': form})


class TaskView(View):
    def get(self, request, *args, **kwargs):
        tasks_id = kwargs.get('task_id')
        task = Tasks.objects.get(pk=tasks_id)
        return render(request, 'tasks/show.html', context={
            'task': task,
        })


class TaskAllView(View):
    def get(self, request, *args, **kwargs):
        tasks = Tasks.objects.all()[:15]
        return render(request, 'tasks/show_all.html', context={
            'tasks': tasks,
        })


class TaskFileView(View):
    def get(self, request, *args, **kwargs):
        tasks_id = kwargs.get('task_id')
        task = Tasks.objects.get(pk=tasks_id)
        return render(request, 'tasks/show_file.html', context={
            'task': task,
        })