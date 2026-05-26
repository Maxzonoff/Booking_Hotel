from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)


class Amenity(models.Model):  # Услуги, Удобства. Wi-Fi/Бассейн/Можно с животными/...)
    title = models.CharField(max_length=100)


class Town(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Hotel(models.Model):
    STARS = [
        (1, "1 звезда"),
        (2, "2 звезды"),
        (3, "3 звезды"),
        (4, "4 звезды"),
        (5, "5 звезд"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    stars = models.IntegerField(choices=STARS, default=3)  # (1-5)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(Amenity)


class Room(models.Model):
    title = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20)
    type = models.CharField(max_length=100)
    total = models.FloatField()  # Количество номеров данного типа
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class SeasonPrice(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price_per_night = (
        models.FloatField()
    )  # Цена комнаты в указанный промежуток времени. Цена за сутки


class Reservation(models.Model):
    STATUS = [
        ("confirmed", "оплачена, подтверждена"),
        ("check_in", "заселен"),
        ("check_out", "выселен"),
        ("canceled", "отменил или не успел оплатить"),
        ("no_show", "неявка"),
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    check_in = models.DateField()  # (date)
    check_out = models.DateField()  # (date)
    created_at = models.DateTimeField(auto_now_add=True)  # (datetime)
    price = models.FloatField()  # Реальная цена на момент резервации
    status = models.CharField(
        choices=STATUS, default="confirmed"
    )  # confirmed(оплачена, подтверждена), check_in(заселен), check_out(выселен), canceled(отменил или не успел оплатить), no_show(неявка)


class Token(models.Model):
    token_hash = models.CharField(max_length=150)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
