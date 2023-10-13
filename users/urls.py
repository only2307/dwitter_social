from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.sign_in, name="login"),
    path("logout/", views.sign_out, name="logout"),
    path("password_change/", views.change_pass, name="password_change"),
    path("password_change_done/", views.change_done, name="password_change_done"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("check_username/", views.check_username, name="check_username"),
    path("register/", views.sign_up, name="register"),
    path("oauth/", include("social_django.urls")),
]