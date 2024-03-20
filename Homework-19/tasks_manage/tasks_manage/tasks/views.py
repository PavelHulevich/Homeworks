from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import UpdateView

# from .forms import ArticleForm
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