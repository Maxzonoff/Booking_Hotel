from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from booking.constants import ReservationStatus
from booking.models import Hotel, Reservation
from booking.serializers import (
    HotelSerializer,
    ReservationListSerializer, ReservationSerializer,
)


class HotelListAPIView(generics.ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class ReservationsListAPIView(generics.ListAPIView):
    serializer_class = ReservationListSerializer
    queryset = Reservation.objects.all()

class ReservationsCreateAPIView(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class ReservationsUpdateAPIView(APIView):

    def patch(self, request, id):
        try:
            reservation = Reservation.objects.get(room_id=id)
        except Reservation.DoesNotExist:
            return Response({"error": "Бронь не найдена"}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get('status')
        if not new_status:
            return Response({"error": "Укажите status"}, status=status.HTTP_400_BAD_REQUEST)

        allowed = [ReservationStatus.CHECK_IN, ReservationStatus.CHECK_OUT,
                   ReservationStatus.CANCELED, ReservationStatus.NO_SHOW]

        if new_status not in allowed:
            return Response({"error": f"Недопустимый статус"}, status=status.HTTP_400_BAD_REQUEST)

        reservation.status = new_status
        reservation.save()

        return Response({"id": reservation.id, "status": reservation.status})
