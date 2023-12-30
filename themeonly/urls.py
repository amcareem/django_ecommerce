from django.urls import include, path, re_path
from themeonly import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('plain/', views.sample_page, name="plain"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_register/', views.user_register, name="user_register"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="themeonly/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="themeonly/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="themeonly/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="themeonly/password_reset_complete.html"), name="password_reset_complete"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    # If you have any URL patterns that require regular expressions, use re_path() like this:
    # re_path(r'^some-pattern/$', views.some_view, name='some_name'),
]
