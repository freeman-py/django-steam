"""
URL configuration for steam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from games.views import index, catalog, cart, cart_add, cart_delete, wishlist, wishlist_add, wishlist_delete, wishlist_add_cart, game, search_game
from users.views import login, register, logout, profile, add_library


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),

    # path('catalog/', include('games.urls', namespace='games')),

    path('catalog/', catalog, name='catalog'),

    path('cart/', cart, name='cart'),
    path('cart-add/<int:game_id>', cart_add, name='cart-add'),
    path('cart-delete/<int:cart_id>', cart_delete, name='cart-delete'),

    path('catalog/<int:category_id>/', catalog, name='category'),

    # path('catalog/<int:category_id>/page/<int:page>/', catalog, name='category_page'),

    path('wishlist/', wishlist, name='wishlist'),
    path('wishlist-add/<int:game_id>', wishlist_add, name='wishlist-add'),
    path('wishlist-delete/<int:wishlist_id>', wishlist_delete, name="wishlist-delete"),
    path('wishlist-add-cart/<int:game_id>/<int:wishlist_id>', wishlist_add_cart, name='wishlist-add-cart'),
    path('add-library/', add_library, name='add-library'),

    path('game/<int:game_id>', game, name='game'),

    path('search/', search_game, name='search-game'),

    # path('users/', include('users.urls', namespace='users')),
    path('login/', login, name="login"),
    path('logout/', logout, name='logout'),
    path('register/', register, name="register"),
    path('profile/', profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)