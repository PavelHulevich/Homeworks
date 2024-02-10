# from django.shortcuts import render
#
# Create your views here.
from django.http import HttpResponse


def hello_view(request):
    name = request.GET.get("name", "World")
    message = request.GET.get("message", "Have a nice day")

    return HttpResponse(f'Hello, {name}! {message}')
