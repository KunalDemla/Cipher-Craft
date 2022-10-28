from django.urls import path,include
from . import views

urlpatterns = [
    path('ciphers/',views.home,name='cipher_list'),
    path('ciphers/<str:cipher_choice>/', views.ciphers,name='ciphers'),
]