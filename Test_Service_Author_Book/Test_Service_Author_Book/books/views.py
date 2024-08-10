from django.shortcuts import render, redirect
from django.views import View

from books.models import Book
from .forms import BookForm
from .models import Book


class BookFormCreateView(View):    # добавление автора в БД
    def get(self, request,  *args, **kwargs):
        form = BookForm()
        return render(request, 'books/create2.html',
                      {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')
        return render(request, 'books/create2.html', {'form': form})


class BookFormEditView(View):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        book = Book.objects.get(id=book_id)
        form = BookForm(instance=book)
        return render(request, 'books/update.html', {'form': form, 'book_id': book_id})

    def post(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        book = Book.objects.get(id=book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books')
        return render(request, 'books/update.html', {'form': form, 'book_id': book_id})


class BookAllView(View):  # просмотр всех авторов из БД
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()[:35]
        return render(request, 'books/show_all.html', context={
            'books': books,
        })


class BookView(View):  # просмотр автора из БД по id
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        book = Book.objects.get(pk=book_id)
        # book = book.fk_book_to_book.name
        return render(request, 'books/show.html', context={
            'book': book,
            'book': book.fk_book_to_book.name,
        })


class BookFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        book = Book.objects.get(id=book_id)
        if book:
            book.delete()
        return redirect('/books')


class BookAllFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        book = Book.objects.all()
        if book:
            book.delete()
        return redirect('/books')
