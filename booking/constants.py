class ReservationStatus:
    CONFIRMED = "confirmed"
    CHECK_IN = "check_in"
    CHECK_OUT = "check_out"
    CANCELED = "canceled"
    NO_SHOW = "no_show"

    CHOICES = [
        (CONFIRMED, "Оплачена, подтверждена"),
        (CHECK_IN, "Заселен"),
        (CHECK_OUT, "Выселен"),
        (CANCELED, "Отменена"),
        (NO_SHOW, "Неявка"),
    ]
