from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from booking.constants import ReservationStatus


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Amenity(models.Model):
    """Услуги, Удобства. Wi-Fi/Бассейн/Можно с животными/..."""

    title = models.CharField(max_length=100, unique=True)


class Town(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "country"], name="unique_town_in_country"
            )
        ]


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    stars = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(Amenity)


class Room(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class SeasonPrice(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=ReservationStatus.CHOICES,
        default=ReservationStatus.CONFIRMED,
    )
