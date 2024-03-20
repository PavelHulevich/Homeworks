from django.shortcuts import render
from django.views import View
from .models import Users, Profiles


class UsersProfileView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = Users.objects.get(pk=user_id)
        profile = Profiles.objects.get(pk=user_id)
        return render(request, 'users/show.html', context={
            'user': user, 'profile': profile
        })
