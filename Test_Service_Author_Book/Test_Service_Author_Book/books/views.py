from django.shortcuts import render, redirect
from django.views import View

from authors.models import Author
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
        author = Author.objects.get(pk=book.fk_book_to_author)
        return render(request, 'books/show.html', context={
            'book': book,
            'author': author,
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
