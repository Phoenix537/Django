from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", LoginView.as_view(template_name='account/login.html')),
    path("logout/", LogoutView.as_view(template_name='account/logout.html')),
    path("register/", views.register, name="register"),
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]