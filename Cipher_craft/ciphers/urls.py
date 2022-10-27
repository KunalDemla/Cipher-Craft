from django.urls import path,include
from . import views

urlpatterns = [
    # path('/'),
    path('caesar/', views.caesar,name='caesar_cipher'),
]