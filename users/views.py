from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import Library
from games.models import Cart


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message='Your account has been created')
            return HttpResponseRedirect(reverse('login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()

    context = {'form': form}


    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message='Your data has been successfully updated')
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=request.user)

    libraries = Library.objects.filter(user=request.user)

    context = {'form': form,
               'libraries': libraries,
    }
    return render(request, 'users/profile.html', context)


@login_required
def add_library(request):
    carts = Cart.objects.filter(user=request.user)
    libraries = Library.objects.filter(user=request.user)

    library_game_ids = libraries.values_list('game_id', flat=True)

    for cart in carts:
        if cart.game.id not in library_game_ids:
            Library.objects.create(user=request.user, game=cart.game)
            cart.delete()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

























