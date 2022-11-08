from re import template
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='user_logout'),
    path('profile/',views.Profile,name='user_profile'),
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'),name='password_reset'),
    path('reset-password-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset-password/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('fav/<str:cipher_choice>/',views.favourite_add,name='favourite_add'),
    path('favourites/',views.show_favourites,name='show_favourites')
]