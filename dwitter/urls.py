from django.urls import path, include
from . import views
app_name = "dwitter"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    #path("accounts/", include("django.contrib.auth.urls")),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>", views.profile, name="profile"),
]