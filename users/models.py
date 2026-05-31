import hashlib
import secrets

from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token_hash = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @classmethod
    def generate_token(cls):
        return secrets.token_urlsafe(32)

    @classmethod
    def hash_token(cls, token):
        return hashlib.sha256(token.encode()).hexdigest()

    def __str__(self):
        return f"Token for {self.user.username}"
