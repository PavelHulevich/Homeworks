from django.urls import path

from .views import UsersProfileView

urlpatterns = [
    path('<user_id>/profile', UsersProfileView.as_view()),
]