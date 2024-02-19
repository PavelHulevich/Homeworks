from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views import View


def index(request: WSGIRequest):
    return HttpResponse("Hello, players.")
