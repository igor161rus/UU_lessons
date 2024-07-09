import json

from django.shortcuts import render, redirect, get_object_or_404

from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse


def logout_view(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def advertisement_list(request):
    advertisements = Advertisement.objects.all()
    # adv_user_count = Advertisement.objects.filter(likes__id=request.user.id).count()
    adv_user_count = Advertisement.objects.filter(likes__id=request.user.id).count()

    print(adv_user_count)
    return render(request, 'board/advertisement_list.html', {'advertisements': advertisements})


def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    context = {
        'advertisement': advertisement,
    }
    likes_connected = get_object_or_404(Advertisement, id=pk)
    liked = False
    if likes_connected.likes.filter(id=request.user.id).exists():
        liked = True
    context['number_of_likes'] = likes_connected.number_of_likes(),
    context['post_is_liked'] = liked

    return render(request, 'board/advertisement_detail.html', context=context)


@login_required
def add_advertisement(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            img_obj = form.instance
            return redirect('board:advertisement_detail', pk=img_obj.pk)
            # return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'board/add_advertisement.html', {'form': form})


@login_required
def edit_advertisement(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            img_obj = form.instance
            return redirect('board:advertisement_detail', pk=img_obj.pk)
            # return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'board/edit_advertisement.html', {'form': form, 'advertisement': advertisement})


@login_required
def delete_advertisement(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        advertisement.delete()
        return redirect('board:advertisement_list')
    return render(request, 'board/delete_advertisement.html', {'advertisement': advertisement})


def post_like(request, pk):
    post = get_object_or_404(Advertisement, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('board:advertisement_detail', args=[str(pk)]))
