from django.urls import path

from .views import TaskView, TaskAllView, TaskFileView

urlpatterns = [
    path('<task_id>/file', TaskFileView.as_view()),
    path('<task_id>/', TaskView.as_view()),
    path('', TaskAllView.as_view()),
]