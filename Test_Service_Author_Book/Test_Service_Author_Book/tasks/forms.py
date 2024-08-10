from django.forms import ModelForm
from .models import Tasks


class TaskForm(ModelForm):

    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'file', 'date_of_create', 'deadline']
