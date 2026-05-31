from django.urls import path
from users.views import RegisterView, LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path("api/v1/register/", RegisterView.as_view(), name="register"),
    path("api/v1/login/", LoginView.as_view(), name="login"),
    path("api/v1/logout/", LogoutView.as_view(), name="logout"),
]
