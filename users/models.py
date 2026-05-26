from tkinter.constants import CASCADE

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_name = None
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )

    token = models.ForeignKey(Token, on_delete=models.CASCADE)
