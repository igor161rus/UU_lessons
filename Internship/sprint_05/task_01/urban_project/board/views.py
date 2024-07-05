from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


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
    return render(request, 'board/advertisement_list.html', {'advertisements': advertisements})


def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    return render(request, 'board/advertisement_detail.html', {'advertisement': advertisement})


@login_required
def add_advertisement(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.author = request.user
            advertisement.save()
            return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'board/add_advertisement.html', {'form': form})


@login_required
def edit_advertisement(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, instance=advertisement)
        if form.is_valid():
            form.save()
            return redirect('board:advertisement_list')
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


def count_likes_dislikes(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    if request.user in advertisement.dislikes.all():
        advertisement.dislikes.remove(request.user)
    else:
        advertisement.dislikes.add(request.user)
    if request.user in advertisement.likes.all():
        advertisement.likes.remove(request.user)
    else:
        advertisement.likes.add(request.user)
    advertisement.save()
    advertisement.refresh_from_db()
    print(advertisement.likes.count())
    return render(request, 'board/count_likes.html', {'advertisement': advertisement})
