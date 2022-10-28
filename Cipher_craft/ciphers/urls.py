from django.urls import path,include
from . import views

urlpatterns = [
    # path('/'),
    path('ciphers/<str:cipher_choice>/', views.ciphers,name='ciphers'),
]