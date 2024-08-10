from django.urls import path

from .views import (BookFormCreateView, BookAllView, BookView, BookFormDeleteView, BookAllFormDeleteView,
                    BookFormEditView)

app_name = 'book'

urlpatterns = [
    path('create/', BookFormCreateView.as_view(), name='book_create'),  # добавление книги в БД
    path('edit/<int:id>/', BookFormEditView.as_view(), name='book_update'),  # редактирование книги в БД
    path('<book_id>/', BookView.as_view(), name='BookView'),  # просмотр книги из БД по id
    path('del/all/', BookAllFormDeleteView.as_view(), name='book_all_del'),  # удаление всех книг из БД
    path('del/<int:book_id>/', BookFormDeleteView.as_view(), name='book_del'),  # удаление книги из БД по ID
    path('', BookAllView.as_view(), name='BookAllView')  # просмотр всех книг из БД

]
