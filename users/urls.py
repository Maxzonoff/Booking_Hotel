from django.urls import path
from users.views import RegisterView, GetTokenView, LogoutView

app_name = "users"

urlpatterns = [
    path("api/v1/register/", RegisterView.as_view(), name="register"),
    path("api/v1/token/", GetTokenView.as_view(), name="token"),
    path("api/v1/logout/", LogoutView.as_view(), name="logout"),
]
