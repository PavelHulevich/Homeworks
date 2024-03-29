from django.urls import path

from .views import TaskView, TaskAllView, TaskFileView, TaskFormCreateView, TaskFormDeleteView

urlpatterns = [
    path('create/', TaskFormCreateView.as_view(), name='tasks_create'),
    # path('create/', TaskCreate.as_view()),
    path('<task_id>/file', TaskFileView.as_view(), name='TaskFileView'),
    path('<task_id>/del/', TaskFormDeleteView.as_view(), name='TaskDelete'),
    path('<task_id>/', TaskView.as_view(), name='TaskView'),
    path('', TaskAllView.as_view(), name='TaskAllView')
]