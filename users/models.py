from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Модель создания пользователя """
    username = None
    email = models.EmailField(unique=True, verbose_name="Email почта")
    telegram_id = models.CharField(max_length=25, default=0, verbose_name="Telegram id")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
