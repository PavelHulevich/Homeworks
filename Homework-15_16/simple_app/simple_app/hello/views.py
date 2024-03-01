from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest


def hello_view(request: WSGIRequest):
    name = request.GET.get("name", "World")
    message = request.GET.get("message", "Have a nice day")

    return HttpResponse(f'Hello, {name}! {message}')