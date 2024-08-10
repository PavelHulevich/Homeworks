from django.urls import path

from .views import (AuthorFormCreateView, AuthorAllView, AuthorView, AuthorFormDeleteView)

app_name = 'author'

urlpatterns = [
    path('create/', AuthorFormCreateView.as_view(), name='author_create'),  # добавление автора в БД
    path('<author_id>/', AuthorView.as_view(), name='AuthorView'),  # просмотр автора из БД по id
    path('del/<int:author_id>/', AuthorFormDeleteView.as_view(), name='author_del'),  # удаление автора из БД по ID
    path('', AuthorAllView.as_view(), name='AuthorAllView')  # просмотр всех авторов из БД

]
