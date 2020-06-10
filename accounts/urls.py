from django.urls import path, re_path, include, reverse_lazy
from .views import signup, signup_pending, activate, signin, signout
from django.contrib.auth import views as auth_views


app_name = "accounts"
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signup-pending/", signup_pending, name="signup_pending"),
    re_path(
        r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate,
        name='activate'
        ),
    path("signin/", signin, name="signin"),
    path("signout", signout, name="signout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="accounts/password/password_reset_form.html",
        success_url=reverse_lazy("accounts:password_reset_done"),
        email_template_name="accounts/password/password_reset_email.html"
        ),
        name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password/password_reset_done.html"
        ),
        name="password_reset_done"),
    path(
        "reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password/password_reset_form.html",
            success_url=reverse_lazy("accounts:password_reset_complete")
        ),
        name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password/password_reset_complete.html"
        ),
        name="password_reset_complete"),
]
