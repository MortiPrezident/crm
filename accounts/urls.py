from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import ProfileView

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="accounts/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("profile/", ProfileView.as_view(), name="profile_me"),
    path("logout/", LogoutView.as_view(next_page="accounts:login"), name="logout"),
]
