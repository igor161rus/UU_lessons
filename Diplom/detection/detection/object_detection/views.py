from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy

from .models import *
from .utils import *
from .forms import *

# menu = [
#     {"title": "Главная", "url_name": "home"},
#     {"title": "Приборная доска", "url_name": "dashboard"},
#     {"title": "Войти", "url_name": "login"},
# ]


def home(request):
    posts = ImageFeed.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная'
    }
    return render(request, "object_detection/home.html", context=context)


def about(request):
    return render(request, "object_detection/about.html", {"title": "О сайте"})


@login_required
def dashboard(request):
    return HttpResponse("dashboard")


# def login(request):
#     return HttpResponse("login")


def image(request, pk):
    try:
        image = ImageFeed.objects.get(pk=pk)
        return render(request, "object_detection/image.html", {"image": image})
    except:
        raise Http404


@login_required
def process_image_feed(request, feed_id):
    image_feed = get_object_or_404(ImageFeed, id=feed_id, user=request.user)
    process_image(feed_id)
    return redirect('object_detection:dashboard')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'object_detection/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'object_detection/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
