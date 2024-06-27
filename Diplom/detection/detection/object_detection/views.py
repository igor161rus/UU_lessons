import os
from operator import index

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import logout, login
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django_admin_geomap import geomap_context

from .models import *
from .utils import *
from .forms import *

# from .forms import UserForgotPasswordForm, UserSetNewPasswordForm


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'object_detection/user_password_reset.html'
    success_url = reverse_lazy('home')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'object_detection/email/password_subject_reset_mail.txt'
    email_template_name = 'object_detection/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'object_detection/user_password_set_new.html'
    success_url = reverse_lazy('home')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context


# menu = [
#     {"title": "Главная", "url_name": "home"},
#     {"title": "Приборная доска", "url_name": "dashboard"},
#     {"title": "Войти", "url_name": "login"},
# ]


def home(request):
    if request.user.is_authenticated:
        image_feeds = ImageFeed.objects.filter(user=request.user)
        image_loc = ImageFeed.objects.filter(user=request.user).values('image', 'lon', 'lat')
        # image_loc = ImageFeed.objects.all()
        print()
        context = {
            # 'location': geomap_context(ImageFeed.objects.filter(user=request.user)),
            'image_feeds': image_feeds,
            'menu': menu,
            'title': 'Главная',
        }
        # return render(request, 'object_detection/home.html',
        #               geomap_context(ImageFeed.objects.filter(user=request.user)))
        return render(request, 'object_detection/home.html',
                      context)
    else:
        return render(request, 'object_detection/home.html', {'menu': menu, 'title': 'Главная'})


def about(request):
    return render(request, "object_detection/about.html", {"title": "О сайте"})


@login_required
def dashboard(request):
    # return render(request, 'object_detection/dashboard.html', {'image_feeds': image_feeds})
    # return HttpResponse("dashboard")
    image_feeds = ImageFeed.objects.filter(user=request.user)
    if not image_feeds:
        return redirect('add_image_feed')
    else:
        # posts = ImageFeed.objects.all()
        x = [x.object_type for x in DetectedObject.objects.filter(image_feed__in=image_feeds)]
        y = [y.confidence for y in DetectedObject.objects.filter(image_feed__in=image_feeds)]
        if x and y:
            chart = get_plot(x, y, 'bar')
            # x = [x.method_detected for x in DetectedObject.objects.filter(image_feed__in=image_feeds)]
            detect_stat = [y for y in
                           DetectedObject.objects.filter(image_feed__in=image_feeds).values('method_detected').annotate(
                               Count('method_detected'))]
            x = []
            y = []
            for i in detect_stat:
                x.append(i['method_detected'])
                y.append(i['method_detected__count'])
            chart_stat = get_plot(x, y, 'line')
        else:
            chart = None
            chart_stat = None

        context = {
            'image_feeds': image_feeds,
            'menu': menu,
            'title': 'Главная',
            'chart': chart,
            'chart_stat': chart_stat
        }
    # read_exif_data(41)
    return render(request, "object_detection/dashboard.html", context=context)


# def login(request):
#     return HttpResponse("login")


def image(request, pk):
    try:
        image = ImageFeed.objects.get(pk=pk)
        return render(request, "object_detection/image.html", {"image": image})
    except:
        raise Http404


def image_detect(request, pk):
    try:
        image = DetectedObject.objects.get(pk=pk)
        return render(request, "object_detection/image_detect.html", {"image": image})
    except:
        raise Http404


@login_required
def process_image_feed(request, feed_id):
    image_feed = get_object_or_404(ImageFeed, id=feed_id, user=request.user)
    process_image(feed_id)
    process_image_detr(feed_id)
    return redirect('dashboard')


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
        return redirect('dashboard')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'object_detection/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('dashboard')


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def add_image_feed(request):
    if request.method == 'POST':
        form = ImageFeedForm(request.POST, request.FILES)
        if form.is_valid():
            image_feed = form.save(commit=False)
            image_feed.user = request.user
            image_feed.lat = 0
            image_feed.lon = 0
            image_feed.save()
            return redirect('dashboard')
    else:
        form = ImageFeedForm()
    return render(request, 'object_detection/add_image_feed.html', {'form': form})


@login_required
def delete_image(request, pk):
    image = get_object_or_404(ImageFeed, id=pk, user=request.user)
    image_det = DetectedObject.objects.filter(image_feed_id=pk).values('processed_image')
    # image_det = get_list_or_404(DetectedObject, image_feed_id=pk)

    if image_det:
        for i in image_det:
            print(image.image.path.strip(), i)
            print(0, i['processed_image'], '\n')
            os.remove(os.path.join(settings.MEDIA_ROOT, i['processed_image']))
    if os.path.exists(image.image.path):
        os.remove(image.image.path)
    image.delete()
    return redirect('dashboard')


def category(request, cat_id):
    return index(request)


def image_detect(request, pk):
    # image = get_object_or_404(ImageFeed, id=pk, user=request.user)
    # print(image, '\n')
    # for i in image.detected_objects.all():
    #     print(i.processed_image)
    # query_set = DetectedObject.objects.filter(image_feed=pk).values('image_feed_id', 'object_type',
    #                                                                 'method_detected', 'confidence',
    #                                                                 'processed_image')

    image_feeds = ImageFeed.objects.filter(user=request.user, id=pk)

    x = [x.object_type for x in DetectedObject.objects.filter(image_feed__in=image_feeds)]
    y = [y.confidence for y in DetectedObject.objects.filter(image_feed__in=image_feeds)]
    if x and y:
        chart = get_plot(x, y, 'bar')
    else:
        chart = None

    context = {'image_feeds': image_feeds,
               'chart': chart,
               'menu': menu,
               }
    return render(request, "object_detection/image_detect.html", context=context)
