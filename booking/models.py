from django.db import models

from users.models import User


class Country(models.Model):

    name = models.CharField()


class Town(models.Model):
    name = models.CharField()
    country = models.CharField()


class Amenity(models.Model):  # Услуги, Удобства. Wi-Fi/Бассейн/Можно с животными/...)
    title = models.CharField()


class Hotel(models.Model):
    STARS = [
        (1, "1 звезда"),
        (2, "2 звезды"),
        (3, "3 звезды"),
        (4, "4 звезды"),
        (5, "5 звезд"),
    ]

    title = models.CharField()
    description = models.TextField()
    stars = models.IntegerField(choices=STARS, default=3)  # (1-5)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    amenities = models.CharField()


class Room(models.Model):
    title = models.CharField()
    type = models.CharField()
    total = models.FloatField()  # Количество номеров данного типа
    hotel = models.CharField()


class SeasonPrice(models.Model):
    room = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    price_per_night = models.FloatField()  # Цена за сутки
    price = models.FloatField()  # Цена комнаты в указанный промежуток времени.


class Reservation:
    STATUS = [
        ("confirmed", "оплачена, подтверждена"),
        ("check_in", "заселен"),
        ("check_out", "выселен"),
        ("canceled", "отменил или не успел оплатить"),
        ("no_show", "неявка"),
    ]
    room = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()  # (date)
    check_out = models.DateField()  # (date)
    created_at = models.DateTimeField()  # (datetime)
    price = models.FloatField()  # Реальная цена на момент резервации
    status = models.CharField(
        choices=STATUS, default="canceled"
    )  # confirmed(оплачена, подтверждена), check_in(заселен), check_out(выселен), canceled(отменил или не успел оплатить), no_show(неявка)


class Token:
    token = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token_hash = models.CharField()
    is_active = False
    created_at = models.DateTimeField()
