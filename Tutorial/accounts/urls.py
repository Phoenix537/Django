from django.urls import path, include
from . import views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, 
    PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", LoginView.as_view(template_name='account/login.html')),
    path("logout/", LogoutView.as_view(template_name='account/logout.html')),
    path("register/", views.register, name="register"),
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"), 
    path("reset-password/", PasswordResetView.as_view(template_name='account/reset_password.html'), name="reset_password"),
    path("reset-password/done/", PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name="password_reset_done"),
    path("reset-password/confirm/<uidb64>/<token>", PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset-password/complete/", PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name="password_reset_complete")
]

