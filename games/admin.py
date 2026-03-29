from django.contrib import admin
from games.models import GameCategory, Game, Cart, Wishlist

# Register your models here.

admin.site.register(GameCategory)
admin.site.register(Cart)
admin.site.register(Wishlist)

@admin.register(Game)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['-price']
    fields = (('name', 'price', 'discount', 'category'), 'description', 'image')



class CartAdminInLine(admin.TabularInline):
    model = Cart
    fields = ('game', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0