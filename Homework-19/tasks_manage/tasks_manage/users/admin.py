from django.contrib import admin

from .models import Users, Profiles, UsersTasks

# admin.site.register(Users)
# admin.site.register(Profiles)
# admin.site.register(UsersTasks)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')


@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('phone', 'status', 'profile')


@admin.register(UsersTasks)
class UsersTasksAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'task_id')
