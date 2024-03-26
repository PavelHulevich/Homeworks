from django.contrib import admin

from .models import Tasks

# admin.site.register(Tasks)
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'deadline')
    list_filter = ('status', 'deadline')
    