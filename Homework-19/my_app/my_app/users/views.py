import datetime
from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import CreationForm, FeedbackForm
from .forms import UserRegistrationForm
from .forms import LoginForm
from .models import Feedback



def order_info(request, user_id, order_id):
    """
    Представление информации о заказе.
    """
    print(request)

    path = reverse('users:order_info', kwargs={'user_id': 42, 'order_id': 101})

    return HttpResponse(f"Order info for user {user_id} and order {order_id}. {path}")


from django.template import Context, Template


def index(request):
    content = """{{user_name}} {{user_surname}} was born in {{year}}"""
    template = Template(content)
    context = Context({"user_name": "Ivan", "user_surname": "Petrov", "year": 1990})

    result = template.render(context)
    return HttpResponse(result)


def index2(request):
    return render(
        request,
        "index.txt",
        {"user_name": "Ivan", "user_surname": "Petrov", "year": 1990}
    )


from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "index.txt"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = 'Ivan'
        context['user_surname'] = 'Petrov'
        context['year'] = 1990
        return context


def petrov(request):
    return render(
        request,
        "petrov.html",
        {"user_name": "Ivan", "user_surnam222e": "Petrov", "year": 1990},
    )


def sidorov(request):
    data = {
        "user_name": "Ivan",
        "user_surname": "Sidorov",
        "year": 1990,
        "male": True,
        "eye_color": "Green",
        "salary_gross": 96,
        "salary_net": 95,
    }
    return render(request, "sidorov.html", data)


@login_required
def profile(request):
    """
    Представление профиля пользователя.
    """
    return render(request, 'users/profile.html')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('store:home')
    template_name = 'users/signup.html'


def feedback_processing(request):
    """
    Представление приема и обработки для обратной связи.
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback(
                feedback_name=form.cleaned_data['feedback_name'],
                feedback_email=form.cleaned_data['feedback_email'],
                feedback_message=form.cleaned_data['feedback_message'],
            )
            feedback.save()

            return render(request, 'users/feedback_success.html')
    return render(request, 'users/feedback_failed.html')


def listing(request):
    data = {
        "my_text": "Hello <b>world</b>",
        "goodies": ["попкорн", "арахис", "кола"],
        "movies": [
            (
                "Citizen Kane",   # Movie
                date(year=1941, month=9, day=5),             # Year
            ),
            (
                "Casablanca",
                date(year=1942, month=9, day=5),
            ),
            (
                "Psycho",
                date(year=1960, month=9, day=5),
            ),
        ]
    }
    return render(request, "listing.html", data)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        next = request.GET['next']
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(next) or HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/sign-in.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponse('Logged out successfully')

