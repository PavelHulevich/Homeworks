from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

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
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('TaskAllView')
        return render(request, 'tasks/create2.html', {'form': form})


class TaskDeleteView(View):
    def get(self, request,  *args, **kwargs):
        task_id = kwargs.get('task_id')
        # task = Tasks.objects.get(pk=task_id)
        return render(request, 'tasks/task_del.html', context={
            'task_id': task_id,
        })

    def delete(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id')
        task = Tasks.objects.get(pk=task_id)
        if task:
            task.delete()
        return redirect('tasks:TaskAllView')


class TaskView(View):
    def get(self, request, *args, **kwargs):
        tasks_id = kwargs.get('task_id')
        task = Tasks.objects.get(pk=tasks_id)
        return render(request, 'tasks/show.html', context={
            'task': task,
        })


class TaskAllView(View):
    def get(self, request, *args, **kwargs):
        tasks = Tasks.objects.all()[:35]
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


class TaskDelete(DeleteView):
    model = Tasks
    success_url = reverse_lazy('TaskDelete')

