from django.urls import path

from .views import (
    ArticleFormDeleteView,
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,

ArticleList,
ArticleDetail,
ArticleCreate,
ArticleUpdate,
    ArticleDelete,
)

urlpatterns = [
    #path('', IndexView.as_view(), name='articles'),
    #path('<int:id>/', ArticleView.as_view()),
    #path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    #path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    #path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),


    path('articles', ArticleList.as_view(), name='articles2'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article2'),
    path('articles-create/', ArticleCreate.as_view(), name='articles2-create'),
    path('articles-update/<int:pk>/', ArticleUpdate.as_view(), name='articles2-update'),
    path('articles-delete/<int:pk>/', ArticleDelete.as_view(), name='articles2-delete'),
]
