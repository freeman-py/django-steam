from django.contrib.auth.models import AbstractUser
from games.models import Game
from django.db import models


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images/', blank=True)
    nickname = models.CharField(max_length=20)


class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Библиотека для {self.user.username} | Игра {self.game.name}'
