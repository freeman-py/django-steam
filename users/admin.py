from django.contrib import admin
from users.models import User
from games.admin import CartAdminInLine

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (CartAdminInLine,)

