from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from users.models import Token


class RegisterView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.create_user(username=username, password=password)

        raw_token = Token.generate_token()

        token_hash = Token.hash_token(raw_token)
        Token.objects.create(user=user, token_hash=token_hash)

        return Response(
            {
                "message": "Регистрация успешна",
                "token": raw_token,
                "username": username,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"error": "Неверный логин или пароль"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not user.check_password(password):
            return Response(
                {"error": "Неверный логин или пароль"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        raw_token = Token.generate_token()
        token_hash = Token.hash_token(raw_token)
        Token.objects.create(user=user, token_hash=token_hash)
        return Response({"access_token": raw_token})

class LogoutView(APIView):
    def post(self, request):
        return Response({"message": "Выход выполнен"})
