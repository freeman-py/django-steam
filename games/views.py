from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from games.models import GameCategory, Game, Cart, Wishlist


# Create your views here.

def index(request):
    return render(request, "games/index.html")


def game(request, game_id):
    game = Game.objects.get(id=game_id)

    context = {
        'game': game,
    }

    return render(request, "games/game.html", context)


def catalog(request, category_id=None, page=1):
    context = {
        "categories": GameCategory.objects.all()
    }

    page = request.GET.get('page', 1)

    if category_id:
        filtered_games = Game.objects.filter(category_id=category_id)
    else:
        filtered_games = Game.objects.all()

    paginator = Paginator(filtered_games, 3)
    catalog_paginator = paginator.get_page(page)

    context['games'] = catalog_paginator
    context['category_id'] = category_id

    return render(request, "games/catalog.html", context)


@login_required
def cart(request):
    carts = Cart.objects.filter(user=request.user)
    total_quantity = carts.count()
    total_sum = sum(crt.game.price for crt in carts)

    context = {
        'carts': carts,
        'total_quantity': total_quantity,
        'total_sum': total_sum,
    }

    return render(request, "games/cart.html", context)


@login_required
def cart_add(request, game_id):
    game = Game.objects.get(id=game_id)
    carts = Cart.objects.filter(user=request.user, game=game)

    if not carts.exists():
        Cart.objects.create(user=request.user, game=game)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def cart_delete(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def wishlist(request):
    wishlists = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlists': wishlists,
    }

    return render(request, "games/wishlist.html", context)


@login_required
def wishlist_add(request, game_id):
    game = Game.objects.get(id=game_id)
    wishlists = Wishlist.objects.filter(user=request.user, game=game)

    if not wishlists.exists():
        Wishlist.objects.create(user=request.user, game=game)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def wishlist_delete(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id)
    wishlist.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def wishlist_add_cart(request, game_id, wishlist_id):
    cart_add(request, game_id)
    wishlist_delete(request, wishlist_id)
    # messages.success(request, message='Товар был успешно перенесен в корзину')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search_game(request):
    games = Game.objects.all()
    query = request.GET.get('q')

    if query:
        games = games.filter(name__icontains=query)

    context = {
        'games': games,
        'query': query,
    }

    return render(request, "games/search.html", context)