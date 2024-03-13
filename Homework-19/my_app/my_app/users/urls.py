from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView
from django.urls import path, reverse_lazy

from .views import (
    SignUp,
    feedback_processing,
    profile,
    order_info, index, index2, IndexView, HomePageView, petrov, sidorov, listing, register, user_login, user_logout
)
from django.views.generic.base import TemplateView

app_name = 'users'

urlpatterns = [
    path('sidorov/', sidorov, name='sidorov'),
    path('petrov/', petrov, name='petrov'),
    path('listing/', listing, name='listing'),

    path('index/', index, name='index'),
    path('index2/', index2, name='index2'),

    path('index3/', IndexView.as_view(), name='index3'),
    path('index4/', TemplateView.as_view(template_name='index.txt')),
    path('index5/', HomePageView.as_view()),



    path('<int:user_id>/orders/<int:order_id>/info/', order_info, name='order_info'),


    path('profile/', profile, name='profile'),
    path('feedback-processing/', feedback_processing, name='feedback_processing'),
    path(
        'auth/logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),

    path('auth/signup/', SignUp.as_view(), name='signup'),

    path(
        'auth/login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login2'
    ),

    path(
        'auth/password_reset/',
        PasswordResetView.as_view(
            template_name='users/managment/password_reset_form.html',
            email_template_name='users/managment/password_reset_email.html',
            success_url='done/'),
        name='password_reset_form'
    ),

    path('auth/password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name='users/managment/password_reset_done.html'),
         name='password_reset_done'),

    path('auth/reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='users/managment/reset_done.html'),
         name='reset_done'),

    path('auth/password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/managment/password_reset_confirm.html',
             success_url=reverse_lazy('users:reset_done')),
         name='password_reset_confirm'),

    path(
        'auth/password_reset_complete/',
        PasswordResetCompleteView.as_view(
            template_name='users/managment/password_reset_complete.html'),
        name='password_reset_complete'
    ),

    path(
        'auth/password_change/',
        PasswordChangeView.as_view(
            template_name='users/managment/password_change_form.html',
            success_url='done/'),
        name='password_change'
    ),
    path(
        'auth/password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/managment/password_change_done.html'),
        name='password_change_done'
    ),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]
