from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import ArticleForm
from .models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:50]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class MyCreateUseCase:

    def create_article(self, dto):
        ...


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')

        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')


class ArticleList(ListView):
    model = Article
    template_name = 'articles/index2.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/show.html'


class ArticleCreate(CreateView):
    model = Article
    #fields = ['name', 'body']
    success_url = reverse_lazy('articles2')
    template_name = 'articles/create2.html'
    form_class = ArticleForm


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['name', 'body']
    success_url = reverse_lazy('articles2')
    template_name = 'articles/update2.html'
    #form_class = ArticleForm


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articles2')


class ArticleList(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/index2.html'