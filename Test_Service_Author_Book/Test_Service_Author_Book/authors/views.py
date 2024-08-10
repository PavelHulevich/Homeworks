from django.shortcuts import render, redirect
from django.views import View

from .forms import AuthorForm
from .models import Author


class AuthorFormCreateView(View):    # добавление автора в БД
    def get(self, request,  *args, **kwargs):
        form = AuthorForm()
        return render(request, 'authors/create2.html',
                      {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/authors')
        return render(request, 'authors/create2.html', {'form': form})


class AuthorFormEditView(View):
    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('id')
        author = Author.objects.get(id=author_id)
        form = AuthorForm(instance=author)
        return render(request, 'authors/update.html', {'form': form, 'author_id':author_id})

    def post(self, request, *args, **kwargs):
        author_id = kwargs.get('id')
        author = Author.objects.get(id=author_id)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('/authors')
        return render(request, 'authors/update.html', {'form': form, 'author_id': author_id})


class AuthorAllView(View):  # просмотр всех авторов из БД
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()[:35]
        return render(request, 'authors/show_all.html', context={
            'authors': authors,
        })


class AuthorView(View):  # просмотр автора из БД по id
    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('author_id')
        author = Author.objects.get(pk=author_id)
        return render(request, 'authors/show.html', context={
            'author': author,
        })


class AuthorFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        author_id = kwargs.get('author_id')
        author = Author.objects.get(id=author_id)
        if author:
            author.delete()
        return redirect('/authors')


class AuthorAllFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        author = Author.objects.all()
        if author:
            author.delete()
        return redirect('/authors')