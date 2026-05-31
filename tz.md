# Сервис для бронирования отелей

Задачи

1. Нужно создать проект на Django
2. Создать приложение users, в котором будут все данные и функционал пользователя (Token, User)
3. Создать приложение Booking, в котором будет вся информация об отелях
4. Авторизация будет через токен, который нужно будет подставлять в headers. При регистрации генерировать хеш токена,
   сохранять его в БД. При проверке брать хеш от access-token и сверять его с базой.
5. Реализовать методы API в соответствии с документацией. Методы не простые, нужно будет валидировать, фильтровать. Так
   же на лету вычислять данные.
6. На первом этапе использовать только ApiView
7. В дальнейшем проект можно расширить, добавить отчеты, и т.д. Но пока остановимся на этом

## Модели

- Country
    - name
- Town
    - name
    - country
- Amenity (Услуги, Удобства. Wi-Fi/Бассейн/Можно с животными/...)
    - title
- Hotel
    - title
    - description
    - stars - (1-5)
    - town
    - amenities
- Room
    - title
    - type
    - total - Количество номеров данного типа
    - hotel
- SeasonPrice
    - room
    - start_date
    - end_date
    - price - Цена комнаты в указанный промежуток времени. Цена за сутки
- Reservation
    - room
    - user
    - check_in (date)
    - check_out (date)
    - created_at (datetime)
    - price - Реальная цена на момент резервации
    - status - confirmed(оплачена, подтверждена), check_in(заселен), check_out(выселен), canceled(отменил или не успел
      оплатить), no_show(неявка)
- Token
    - user
    - token_hash
    - is_active
    - created_at

---

## API

### Регистрация

- Method: POST
- Path: /api/v1/register/
- Request body

```
{
    "username": "...",
    "password": "..."
}
```

- Response

```
{
    "access_token": "..."
}
```

### Логин

- Method: POST
- Path: /api/v1/login/
- Request body

```
{
    "username": "...",
    "password": "..."
}
```

- Response

```
{
    "access_token": "..."
}
```

### Логаут

- Permission: IsAuthenticated
- Method: POST
- Path: /api/v1/logout/
- Request headers

```
{
    "x-access-token": "Token ...",
}
```

### Список отелей

- Permission: Any
- Method: GET
- Path: /api/v1/hotels/
- Request query params

```
{
    "check_in": "20.06.2026",   // Обязательно
    "check_out": "25.06.2026",  // Обязательно
    "town_id": 1,
    "start": 3,  // 3 и более звезд
    "amenities": ["Wi-Fi", "Бассейн"]
}
```

- Response body

```
{
    "count": 150,
    "next": "https:...",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "...",
            "description": "...",
            "start": 4,
            "town": {
                "id": 1,
                "name": "Египет"
            },
            "amenities": [...],
            "min_price": 5000,  // Минимальная цена свободных номеров за указанный период
            "max_price": 8000,  // Минимальная цена свободных номеров за указанный период
        }
    ]
}
```

### Карточка отеля и список свободных номеров

- Permission: IsAuthenticated
- Method: POST
- Path: /api/v1/reservations/
- Request body

```
{
    "room_id": 4,
    "check_in": "20.06.2026",
    "check_out": "25.06.2026"
}
```

- Response body

```
{
    "id": 12,
    "room": 4,
    "user": 2,
    "check_in": "20.06.2026",
    "check_out": "25.06.2026",
    "created_at": "21.05.2026T14:30:00Z",
    "price": 25000, 
    "status": "confirmed"
}
```

### Список бронирований текущего пользователя

- Permission: IsAuthenticated, только свои брони
- Method: GET
- Path: /api/v1/reservations/
- Response body

```
[
    {
        "id": 12,
        "room_title": "Стандарт Double",
        "hotel_title": "Grand Hotel",
        "check_in": "20.06.2026",
        "check_out": "25.06.2026",
        "price": 25000,
        "status": "confirmed"
    }
]
```

### Изменение статуса бронирования

- Permission: IsAuthenticated, только свои брони
- Method: PATCH
- Path: /api/v1/reservations/{id}/change_status/
- Request body

```
{
    "status": "canceled",  // Одно из значений: check_in, check_out, canceled, no_show
}
```