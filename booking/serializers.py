from rest_framework import serializers

from booking.models import Hotel, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class ReservationListSerializer(serializers.ModelSerializer):
    room_title = serializers.CharField(source="room.title", read_only=True)
    hotel_title = serializers.CharField(source="room.hotel.title", read_only=True)

    class Meta:
        model = Reservation
        fields = [
            "id",
            "room_title",
            "hotel_title",
            "check_in",
            "check_out",
            "price",
            "status",
        ]
