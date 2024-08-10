from django.shortcuts import render
from django.views import View


class HelloView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'hello/hello.html')


