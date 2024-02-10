from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def index(request: WSGIRequest):
    return HttpResponse("Hello, players.")
