from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from users.models import Token


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        auth_header = request.headers.get("Authentication")
        if not auth_header:
            raise AuthenticationFailed("Токен не указан")

        auth_parts = auth_header.split()
        if len(auth_parts) != 2:
            raise AuthenticationFailed("Токен указан не верно")

        token_type, raw_token = auth_parts

        token = Token.objects.filter(token_hash=Token.hash_token(token=raw_token)).first()
        if not token:
            raise AuthenticationFailed("Токен указан не верно")

        return token.user, token

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        return "Token"