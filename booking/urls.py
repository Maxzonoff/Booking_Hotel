from django.urls import path

from booking.views import (
    HotelListAPIView,
    ReservationsListAPIView,
    ReservationsUpdateAPIView, ReservationsCreateAPIView,
)

app_name = "booking"

urlpatterns = [
    path("api/v1/hotels/", HotelListAPIView.as_view(), name="hotels"),
    path(
        "api/v1/reservations/", ReservationsListAPIView.as_view(), name="reservations"
    ),
    path("api/v1/reservations/create/", ReservationsCreateAPIView.as_view(), name="reservations_create"),
    path(
        "api/v1/reservations/<int:id>/change_status/",
        ReservationsUpdateAPIView.as_view(),
        name="change_status",
    ),

]
