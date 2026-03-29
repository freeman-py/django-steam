from django.db import models
# from users.models import User
# Create your models here.
# Модель = таблица БД

class GameCategory(models.Model):
    genre = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.genre


class Game(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='games_images/', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # quantity = models.PositiveIntegerField(default=1)  НЕ НУЖНО!!!
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE) # PROTECT
    discount = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.category.genre}"


class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.nickname} | Игра {self.game.name}'

    # def sum(self):
    #     return self.game.price


class Wishlist(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Список желаемого для {self.user.username} | Игра {self.game.name}'
