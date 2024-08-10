from django.urls import path
from .views import HelloView

app_name = 'hello'

urlpatterns = [
    path('', HelloView.as_view(), name='hello_view')
]