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
from .models import Users, Profiles


class UsersProfileView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = Users.objects.get(pk=user_id)
        profile = Profiles.objects.get(pk=user_id)
        return render(request, 'users/show.html', context={
            'user': user, 'profile': profile
        })
